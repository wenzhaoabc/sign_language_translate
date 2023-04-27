# -*- coding: utf-8 -*-
"""
网络请求API
"""
import asyncio
import io
import sys
from flask_socketio import SocketIO, emit
from PIL import Image
import json
import pymysql.cursors
from flask import request, session

sys.path.append('D:\\WorkSpace\\Python\\sign_language\\sign_language_translate\\')
sys.path.append('/workspace/python/sign')

from network import trans_model
from api import create_app
from dbconn import get_db
from utils import allow_cors, ResponseCode, verify_phone, upload_image, DatetimeEncoder, response_json, upload_file

app = create_app()
app.after_request(allow_cors)
app.after_request(response_json)


# region


@app.route('/register', methods=['POST'])
def register():
    """
    用户注册，post请求，请求体位于body
    ```json
    {
        "phone": "string, 用户手机号",
        "password": "string,哈希加密后的密码",
        "username": "string,用户昵称",
        "avatar": "base64格式，用户头像图片"
    }
    ```
    :return: data字段 注册成功返回userInfo 其余为空
    """
    # 获取request的body里面的数据
    body_data = request.get_json()
    username = body_data.get('username', 'User')
    phone = body_data.get('phone')
    password = body_data.get('password')
    avatar = body_data.get('avatar')
    # 获取数据库连接
    db_conn = get_db()
    # response
    code = ResponseCode.success
    msg = ''
    userInfo = None

    if not phone:
        code = ResponseCode.param_missing
        msg = '缺少手机号'
    elif not verify_phone(phone):
        code = ResponseCode.param_error
        msg = '手机号格式错误'
    elif not password:
        code = ResponseCode.param_missing
        msg = '缺少密码'
    else:
        pass

    if avatar and avatar != '':
        try:
            avatar = upload_image(avatar)
        except RuntimeError:
            avatar = None

    if code is ResponseCode.success:
        cursor = db_conn.cursor(pymysql.cursors.DictCursor)
        try:
            cursor.execute("SELECT id FROM t_user WHERE phone = %s", (phone))
            result = cursor.fetchone()
            if result:
                code = ResponseCode.existed_error
                msg = '该手机号已注册'
            else:
                try:
                    cursor.execute(
                        "INSERT INTO db_sign.t_user(phone,username,password,avatar) VALUES (%s,%s,%s,%s)",
                        (phone, username, password, avatar))
                    db_conn.commit()
                    code = ResponseCode.success
                    msg = '已成功注册'
                    cursor.execute(
                        "SELECT id, phone,username,avatar,created FROM db_sign.t_user WHERE phone = %s", (phone))
                    userInfo = cursor.fetchone()
                    session.clear()
                    session['user_id'] = userInfo['id']
                    session['user_phone'] = userInfo['phone']
                except db_conn.IntegrityError:
                    code = ResponseCode.existed_error
                    msg = '该手机号已注册'
        except db_conn.Error:
            pass
        finally:
            # 释放游标
            cursor.close()
    result = dict(code=code, data=userInfo, msg=msg)
    return json.dumps(result, cls=DatetimeEncoder)


@app.route('/login', methods=['POST'])
def user_login():
    """
    用户登录，post请求，请求体位于body
    ```json
    {
        "phone": "string,用户手机号",
        "password": "string,哈希加密后的密码"
    }
    ```
    :return: 登陆成功返回userInfo,其余情况为空
    """
    body_data = request.get_json()
    phone = body_data.get('phone')
    password = body_data.get('password')
    code = ResponseCode.success
    msg = ''
    userInfo = None

    if not phone:
        code = ResponseCode.param_missing
        msg = '缺少手机号'
    elif not verify_phone(phone):
        code = ResponseCode.param_error
        msg = '手机号不合法'
    elif not password:
        code = ResponseCode.param_missing
        msg = '密码错误'
    else:
        pass

    if code is ResponseCode.success:
        db_conn = get_db()
        cursor = db_conn.cursor(pymysql.cursors.DictCursor)
        try:
            cursor.execute(
                "SELECT id, phone,username,avatar,created FROM db_sign.t_user WHERE phone = %s AND password = %s",
                (phone, password))
            userInfo = cursor.fetchone()
            if not userInfo:
                code = ResponseCode.db_not_found
                msg = '账号或密码错误'
            else:
                session.clear()
                session['user_id'] = userInfo['id']
                session['user_phone'] = userInfo['phone']
        except db_conn.Error:
            code = ResponseCode.db_conn_error
            msg = '数据库连接错误'
        finally:
            # 释放游标
            cursor.close()

    result = dict(code=code, data=userInfo, msg=msg)
    return json.dumps(result, cls=DatetimeEncoder)


@app.route('/logout', methods=['POST'])
def user_logout():
    """
    用户退出登录
    :return: data域为空
    """
    session.clear()
    result = dict(code=ResponseCode.success, msg='退出登录成功')
    return json.dumps(result)


@app.route('/remove_account', methods=['DELETE'])
def remove_account():
    """
    账户注销，级联删除数据库中用户的有关信息
    :return: data域为空
    """
    user_id = session.get('user_id')
    db_conn = get_db()
    cursor = db_conn.cursor()
    code = ResponseCode.success
    msg = ''

    if user_id:
        try:
            cursor.execute("DELETE FROM db_sign.t_user WHERE id = %s", (int(user_id)))
            db_conn.commit()
            code = ResponseCode.success
            msg = '账户注销成功'
        except db_conn.Error:
            db_conn.rollback()
            code = ResponseCode.db_conn_error
            msg = '数据库错误'
        finally:
            cursor.close()
    else:
        code = ResponseCode.db_not_found
        msg = '账户不存在'
    result = dict(code=code, msg=msg)

    return json.dumps(result)


@app.route('/modify_user_info', methods=['PUT'])
def modify_user_info():
    """
    用户修改个人信息,put请求，请求体位于body中，根据需要修改
    ```json
    {
        "username": "string, 用户名",
        "password": "string,用户登录密码",
        "avatar": "string,用户头像，已base64编码"
    }
    ```
    :return: 修改成功返回新的用户个人信息，否则data域为空
    """
    user_id = session.get('user_id')
    body_data = request.get_json()
    username = body_data.get('username', 'User')
    password = body_data.get('password')
    avatar = body_data.get('avatar')
    code = ResponseCode.success
    msg = ''
    userInfo = None

    db_conn = get_db()
    cursor = db_conn.cursor(pymysql.cursors.DictCursor)

    if user_id:
        try:
            if username:
                cursor.execute("UPDATE db_sign.t_user SET username = %s WHERE id = %s", (username, int(user_id)))
            if password:
                cursor.execute("UPDATE db_sign.t_user SET password = %s WHERE id = %s", (password, int(user_id)))
            if avatar:
                avatar_url = upload_image(avatar)
                cursor.execute("UPDATE db_sign.t_user SET avatar = %s WHERE id = %s", (avatar_url, int(user_id)))
            db_conn.commit()
            code = ResponseCode.success
            msg = '修改成功'
            cursor.execute(
                "SELECT id, phone,username,avatar,created FROM db_sign.t_user WHERE id = %s", (int(user_id)))
            userInfo = cursor.fetchone()
            session.clear()
            session['user_id'] = userInfo['id']
            session['user_phone'] = userInfo['phone']
        except db_conn.Error:
            db_conn.rollback()
            code = ResponseCode.db_conn_error
            msg = '数据库连接错误'
        finally:
            cursor.close()
    else:
        code = ResponseCode.db_not_found
        msg = '用户未登录'

    result = dict(code=code, data=userInfo, msg=msg)
    return json.dumps(result, cls=DatetimeEncoder)


@app.route('/upload_single_image', methods=['POST'])
def upload_image_test():
    """
    以base64的形式上传图片，对于用户头像的上传可以使用该API，上传文件请使用/upload_files
    :return: data域中为访问图片的URL
    """
    body_data = request.get_json()
    base64_img = body_data.get('image')
    image_url = upload_image(base64_img)
    result = dict(url=image_url)
    return json.dumps(result)


@app.route('/upload_files', methods=['POST'])
def flask_upload_files_by_form():
    """
    上传多个文件，文件存在于form中
    :return: data域中为文件名及访问URL
    """
    code = ResponseCode.success
    msg = ''
    data = []

    try:
        for item in request.files.keys():
            file = request.files.get(item)
            file_url = upload_file(file, file.filename)
            file_dict = dict(file=file.filename, url=file_url, success=True)
            data.append(file_dict)
    except IOError:
        data.pop()
        code = ResponseCode.existed_error
        msg = '存在未上传成功的文件'
    finally:
        result = dict(code=code, data=data, msg=msg)
    return json.dumps(result)


@app.route('/add_word', methods=['POST'])
def add_word_item():
    code = ResponseCode.success
    msg = ''
    word_item = dict()

    word = request.form.get('word')
    if word is None:
        code = ResponseCode.param_missing
        msg = '缺少单词名'
    else:
        word_item['word'] = word
        word_item['description'] = request.form['description']
        word_item['notes'] = request.form['notes']
        word_item['type'] = request.form['type']
        word_item['tags'] = request.form['tags']
        file_img = request.files.get('img')
        if (file_img is None) or (file_img.filename is None):
            code = ResponseCode.param_missing
            msg = '缺少说明图片'
            word_item = None
        else:
            word_item['img'] = upload_file(file_img, file_img.filename)
            file_video = request.files.get('video')
            if file_video is not None and file_video.content_length > 0:
                word_item['video'] = upload_file(file_video, file_video.filename)
            else:
                word_item['video'] = None

    if code == ResponseCode.success:
        db_conn = get_db()
        cursor = db_conn.cursor()
        try:
            sql = "INSERT INTO db_sign.t_word(word, description, notes,tags, img, video, `type`) " \
                  "VALUES (%s,%s,%s,%s,%s,%s,%s)"
            values = (
                word_item['word'], word_item['description'], word_item['notes'], word_item['tags'], word_item['img'],
                word_item['video'], word_item['type'])
            cursor.execute(sql, values)
            db_conn.commit()
            msg = '插入成功'
            cursor.execute("SELECT LAST_INSERT_ID() AS id FROM db_sign.t_word")
            word_item['id'] = cursor.fetchone()[0]
        except db_conn.Error:
            db_conn.rollback()
            code = ResponseCode.db_conn_error
            msg = '数据库连接错误'
        finally:
            cursor.close()

    result = dict(code=code, data=word_item, msg=msg)
    return json.dumps(result)


@app.route('/word_list', methods=['GET'])
def get_word_item_all_list():
    code = ResponseCode.success
    msg = 'success'
    data = []

    word = request.args.get('word', type=str)
    word_type = request.args.get('type', type=str)

    word_id = request.args.get('id')
    if word_id is not None:
        try:
            word_id = int(word_id)
        except (TypeError, ValueError):
            code = ResponseCode.param_error
            msg = '数据解析出错'

    db_conn = get_db()
    cursor = db_conn.cursor(pymysql.cursors.DictCursor)

    if code == ResponseCode.success:
        try:
            if word_id is not None:
                cursor.execute("SELECT * FROM db_sign.t_word WHERE id = %s", (word_id))
                data = cursor.fetchone()
            else:
                if (word is None) and (word_type is None):
                    cursor.execute("SELECT * FROM db_sign.t_word")
                    data = cursor.fetchall()
                elif (word is not None) and (word_type is None):
                    cursor.execute("SELECT * FROM db_sign.t_word WHERE LOCATE(%s,word)>0", (word))
                    data = cursor.fetchall()
                elif (word is None) and (word_type is not None):
                    cursor.execute("SELECT * FROM db_sign.t_word WHERE LOCATE(%s,type)>0", (word_type))
                    data = cursor.fetchall()
                else:
                    cursor.execute("SELECT * FROM db_sign.t_word WHERE LOCATE(%s,word)>0 AND LOCATE(%s,type)>0",
                                   (word, word_type))
                    data = cursor.fetchall()
        except db_conn.Error:
            data = None
            code = ResponseCode.db_conn_error
            msg = '数据库连接错误'
        finally:
            cursor.close()

    result = dict(code=code, data=data, msg=msg)
    return json.dumps(result)


@app.route('/love', methods=['POST'])
def add_love_word():
    """
    添加收藏
    """
    code = ResponseCode.success
    msg = ''
    loved_word = request.get_json()
    loved_word['user_id'] = session.get('user_id')

    db_conn = get_db()
    cursor = db_conn.cursor()
    try:
        cursor.execute("SELECT * FROM db_sign.t_word_love WHERE word_id=%s AND user_id=%s",
                       (loved_word['word_id'], loved_word['user_id']))
        if cursor.fetchone() is None:
            cursor.execute("INSERT INTO db_sign.t_word_love(word_id,user_id) VALUES (%s,%s)",
                           (loved_word['word_id'], loved_word['user_id']))
            db_conn.commit()
            msg = 'success'
        else:
            msg = '已收藏'
    except db_conn.Error:
        code = ResponseCode.db_conn_error
        msg = '数据库连接错误'
    finally:
        cursor.close()

    result = dict(code=code, msg=msg, data={})
    return json.dumps(result)


@app.route('/my_loves', methods=['GET'])
def get_all_my_loves():
    """
    获取我的全部收藏
    """
    code = ResponseCode.success
    msg = 'success'
    data = list()

    user_id = session.get('user_id')
    if user_id is None:
        code = ResponseCode.not_logged_in
        msg = '用户未登录'
    else:
        db_conn = get_db()
        cursor = db_conn.cursor(pymysql.cursors.DictCursor)
        try:
            cursor.execute(
                "SELECT t_word.* FROM t_word,t_word_love "
                "WHERE t_word.id = t_word_love.word_id AND t_word_love.user_id = %s",
                (user_id))
            data = cursor.fetchall()
            msg = 'success'
        except db_conn.Error:
            code = ResponseCode.db_conn_error
            msg = '数据库连接错误'
        finally:
            cursor.close()

    result = dict(code=code, data=data, msg=msg)
    return json.dumps(result)


@app.route('/is_loved')
def get_word_is_loved():
    """
    获取当前单词是否已被用户收藏
    """
    code = ResponseCode.success
    msg = ''
    data = ''

    word_id = request.args.get('id')
    if word_id is None:
        code = ResponseCode.param_missing
        msg = '缺失单词ID'

    user_id = session.get('user_id')
    if user_id is None:
        code = ResponseCode.not_logged_in
        msg = '用户未登录'

    if code == ResponseCode.success:
        db_conn = get_db()
        cursor = db_conn.cursor()
        try:
            cursor.execute("SELECT * FROM db_sign.t_word_love WHERE word_id=%s AND user_id=%s",
                           (word_id, user_id))
            data = cursor.fetchone()
            if data is not None:
                data = False
                msg = '用户未收藏'
            else:
                data = True
                msg = '已收藏'
        except db_conn.Error:
            code = ResponseCode.db_not_found
            msg = '数据库连接错误'
        finally:
            cursor.close()

    result = dict(code=code, data=data, msg=msg)
    return json.dumps(result)


@app.route('/cancel_love', methods=['DELETE'])
def cancel_word_love():
    """
    取消收藏
    """
    code = ResponseCode.success
    msg = ''

    word_id = request.args.get('word_id')
    if word_id is None:
        code = ResponseCode.param_missing
        msg = '缺失单词ID'

    user_id = session.get('user_id')
    if user_id is None:
        code = ResponseCode.not_logged_in
        msg = '用户未登录或登录过期'

    if code == ResponseCode.success:
        db_conn = get_db()
        cursor = db_conn.cursor()
        try:
            cursor.execute("DELETE FROM db_sign.t_word_love WHERE word_id = %s AND user_id = %s",
                           (word_id, user_id))
            msg = '取消成功'
        except db_conn.Error:
            code = ResponseCode.db_conn_error
            msg = '数据库连接错误'
        finally:
            cursor.close()

    result = dict(code=code, msg=msg, data=None)
    return json.dumps(result)


# endregion

socket = SocketIO()
socket.init_app(app, cors_allowed_origins='*')


@socket.on("connect")
def handle_connect_video(data):
    emit('response', {'data:': 'connected {}'.format(data)})
    print("client connect")


@socket.on("disconnect")
def handle_disconnect_video():
    print("disconnect")


@socket.on("message")
def handle_video_stream(message):
    print("received message : {}".format(message))


@socket.on("video")
def handle_upload_video_stream(data):
    # print(len(data))
    # print(type(data))
    """V3 - YUV420 """
    # y_length = temp[0] * 255 * 255 + temp[1] * 255 + temp[2]
    # width = temp[3] * 255 + temp[4]
    # Y = temp[5:5 + y_length]
    """"""
    """
    jpeg格式
    需要舍弃前5个字节
    """
    # print(data[0], data[1], data[3], data[len(data) - 1], data[len(data) - 2])
    img = Image.open(io.BytesIO(data[5:]))
    # trans_model.add_image_toQueue1(img)
    asyncio.run(trans_model.add_image(img))


def send_translated_text(text):
    print("_________trans____________res +++++++++++++ = : {}".format(text))
    socket.emit("trans", text)


if __name__ == '__main__':
    socket.run(app, host='0.0.0.0', debug=True, port=5002)
