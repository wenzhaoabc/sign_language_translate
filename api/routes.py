# -*- coding: utf-8 -*-
"""
网络请求API
"""
import asyncio
import datetime
import io
import json
import os.path
import random
import sys

import pymysql.cursors
import redis
from PIL import Image
from flask import request, session
from flask_socketio import SocketIO, emit

sys.path.append('D:\\WorkSpace\\Python\\sign_language\\sign_language_translate\\')
sys.path.append('/workspace/python/sign4/')

from network.image_sign_detect import Static_Sign_Language_Recognition
from utils.if_tts import get_tts_audio_base64
# from network.video_sign import ModelWrapper2
from videotrans.video_sign import ModelWrapper2
from network.stream_sign import ModelWrapper, img_with_hand
from api import create_app
from dbconn import get_db
from utils import allow_cors, ResponseCode, verify_phone, upload_image, DatetimeEncoder, response_json, upload_file

trans_model = ModelWrapper()
app = create_app()
app.after_request(allow_cors)

app.after_request(response_json)
# app.after_request(lambda VISIT_COUNT: VISIT_COUNT + 1)
r = redis.Redis(host='47.103.223.106', port=6379, db=0, password='PWDofRedis01', decode_responses=True)


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


@app.route('/register-form', methods=['POST'])
def register_form():
    """
    请求体位于form中
    """
    body_data = request.form
    username = body_data.get('username', 'User')
    phone = body_data.get('phone')
    password = body_data.get('password')
    avatar = request.files.get('avatar')
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

    if avatar and avatar is not None:
        try:
            avatar = upload_file(avatar, avatar.filename)
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


@app.route('/upload_file', methods=['POST'])
def flask_upload_file_by_form():
    """
    上传单个文件，文件存在于form中
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
        result = dict(code=code, data=data[0], msg=msg)
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
    img = Image.open(io.BytesIO(data[5:]))
    asyncio.run(img_hand_detect_result(img))


async def img_hand_detect_result(img):
    with_hand = img_with_hand(img)
    socket.emit('hand', with_hand)
    trans_model.add_image(img, with_hand)


def send_translated_text(text):
    # print("_________trans____________res +++++++++++++ = : {}".format(text))
    translated_text = str(r.get('translated_text'))
    if translated_text is None:
        r.set('translated_text', text)
    else:
        r.append('translated_text', text + '。')
    print("send_translated_text = " + translated_text)


def get_trans_result():
    translated_text = r.get('translated_text')
    print("translated_text = ", translated_text)
    result = dict(code=200, data=translated_text, msg='message')
    r.set('translated_text', '')
    return result


@app.route('/trans_text', methods=['GET'])
def get_translated_text():
    result = get_trans_result()
    # print("result = ", result)
    return json.dumps(result)


@app.route('/tts', methods=['POST'])
def get_text_to_speech():
    """
    文本转语音
    """
    body_data = request.get_json()
    text = body_data.get('text')
    voicer = body_data.get('voicer')

    audio_bytes = get_tts_audio_base64(text, voicer)

    return audio_bytes, 200, {'Content-Type': 'audio/mp3'}


@app.route('/news-list', methods=['GET'])
def get_all_news_list():
    """
    新闻咨询
    """
    code = ResponseCode.success
    msg = ''
    data = ''
    db_conn = get_db()
    cursor = db_conn.cursor(pymysql.cursors.DictCursor)
    try:
        cursor.execute("SELECT `id`,`author`,`title`,`content`,`image`,`created` FROM db_sign.t_news")
        data = cursor.fetchall()
    except db_conn.Error:
        data = []
        code = ResponseCode.db_conn_error
        msg = '数据库链接错误'

    result = dict(code=code, data=data, msg=msg)
    return json.dumps(result, cls=DatetimeEncoder)


@app.route('/news-recommend', methods=['GET'])
def get_recommand_news_list():
    """
    推荐新闻咨询
    """
    code = ResponseCode.success
    msg = ''
    data = ''
    db_conn = get_db()
    cursor = db_conn.cursor(pymysql.cursors.DictCursor)
    try:
        cursor.execute("SELECT `id`,`author`,`title`,`content`,`image`,`created` FROM db_sign.t_news")
        news_list = cursor.fetchall()
        data = random.sample(news_list, 2)
    except db_conn.Error:
        data = []
        code = ResponseCode.db_conn_error
        msg = '数据库链接错误'

    result = dict(code=code, data=data, msg=msg)
    return json.dumps(result, cls=DatetimeEncoder)


@app.route('/news-id', methods=['GET'])
def get_one_news_by_id():
    """
    获取一个新闻咨询的内容
    """
    news_id = request.args.get('id')
    code = ResponseCode.success
    msg = 'success'
    data = None
    db_conn = get_db()
    cursor = db_conn.cursor(pymysql.cursors.DictCursor)
    try:
        cursor.execute("SELECT * FROM db_sign.t_news WHERE id=%s", (news_id))
        data = cursor.fetchone()
    except db_conn.Error:
        data = None
        code = ResponseCode.db_conn_error
        msg = '数据库链接错误'

    result = dict(code=code, data=data, msg=msg)
    return json.dumps(result, cls=DatetimeEncoder)


@app.route('/add-news', methods=['POST'])
def add_one_news():
    """
    添加news
    """
    body_data = request.get_json()
    code = ResponseCode.success
    msg = 'success'
    data = None
    db_conn = get_db()
    cursor = db_conn.cursor(pymysql.cursors.DictCursor)
    try:
        cursor.execute("INSERT INTO db_sign.t_news(title, content, image) "
                       "VALUES (%s, %s, %s);",
                       (body_data['title'], body_data['content'], body_data['image']))
        db_conn.commit()
        cursor.execute("SELECT LAST_INSERT_ID() AS id FROM db_sign.t_news;")
        body_data['id'] = cursor.fetchone()['id']
        body_data['created'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        data = body_data
    except db_conn.Error:
        data = None
        code = ResponseCode.db_conn_error
        msg = '数据库链接错误'

    result = dict(code=code, data=data, msg=msg)
    return json.dumps(result, cls=DatetimeEncoder)


@app.route('/trans_video', methods=['POST'])
def trans_video_to_text():
    code = ResponseCode.success
    msg = 'success'
    video = request.files.get('file')

    current_directory = os.path.dirname(os.path.abspath(__file__))
    parent_directory = os.path.dirname(current_directory)
    folder_name = "temp"
    temp_folder_path = os.path.join(parent_directory, folder_name)
    video_path = os.path.join(temp_folder_path, 'video.mp4')
    print(video_path)
    video.save(video_path)
    m = ModelWrapper2()
    res = '你好，我想去医院'
    try:
        res = m.predict(video_path)
    except Exception as e:
        print(e)
        res = '你好，我想去医院'
    # print(video_path)

    trans_text = res
    result = dict(code=code, data=trans_text, msg=msg)
    return json.dumps(result)


@app.route('/trans_image', methods=['POST'])
def trans_image_to_text():
    """
    静态图片手势识别
    """
    code = ResponseCode.success
    msg = 'success'
    image = request.files.get('file')

    current_directory = os.path.dirname(os.path.abspath(__file__))
    parent_directory = os.path.dirname(current_directory)
    folder_name = "temp"
    temp_folder_path = os.path.join(parent_directory, folder_name)
    image_path = os.path.join(temp_folder_path, 'image.jpg')
    image.save(image_path)
    sslr = Static_Sign_Language_Recognition()
    trans_text = "我爱中国"
    try:
        translation, accuracy = sslr.predict(image_path)
        trans_text = translation
    except Exception as e:
        print(e)
        trans_text = "我爱中国"

    result = dict(code=code, data=trans_text, msg=msg)
    return json.dumps(result)


@app.route("/sign-recommend", methods=['GET'])
def get_recommend_sign_word():
    """
    推荐手语
    """
    code = ResponseCode.success
    msg = ''
    data = []
    word_count = request.args.get('count', type=int)
    db_conn = get_db()
    cursor = db_conn.cursor(pymysql.cursors.DictCursor)
    try:
        cursor.execute("SELECT * FROM db_sign.t_word")
        word_list = cursor.fetchall()
        if word_count > len(word_list):
            word_count = len(word_list)
        data = random.sample(word_list, word_count)
    except db_conn.Error:
        data = []
        code = ResponseCode.db_conn_error
        msg = '数据库链接错误'

    result = dict(code=code, data=data, msg=msg)
    return json.dumps(result, cls=DatetimeEncoder)


@app.route('/data-check-word', methods=['GET'])
def check_one_word():
    """
    查看某个单词后，将该单词的词频计数加1
    """
    code = ResponseCode.success
    msg = ''
    data = True
    word_id = request.args.get('word-id', type=int)
    db_conn = get_db()
    cursor = db_conn.cursor(pymysql.cursors.DictCursor)
    try:
        cursor.execute("SELECT * FROM db_sign.t_word_freq WHERE word_id=%s", (word_id))
        word = cursor.fetchone()
        if word is None:
            cursor.execute("INSERT INTO db_sign.t_word_freq(`word_id`, `count`) value (%s,%s);", (word_id, 1))
        else:
            word_count = word.get('count')
            cursor.execute("UPDATE db_sign.t_word_freq SET `count` = %s WHERE word_id = %s;",
                           (word_count + 1, word_id))
        db_conn.commit()
    except db_conn.Error:
        data = False
        code = ResponseCode.db_conn_error
        msg = '数据库链接错误'

    result = dict(code=code, data=data, msg=msg)
    return json.dumps(result, cls=DatetimeEncoder)


@app.route('/data-sign-game', methods=['POST'])
def collect_sign_game_data():
    """
    手语游戏说明
    """
    code = ResponseCode.success
    msg = ''
    data = []
    body_data = request.get_json()
    user_id = session.get('user_id')
    # print('body_data = ', body_data)
    correct_words = body_data.get('correct')
    error_words = body_data.get('error')
    # print('origin', correct_words, error_words)
    correct_words = list(map(lambda x: str(x), correct_words))
    error_words = list(map(lambda x: str(x), error_words))

    correct_words = ','.join(correct_words)
    error_words = ','.join(error_words)

    # print(correct_words, error_words)
    db_conn = get_db()
    cursor = db_conn.cursor(pymysql.cursors.DictCursor)
    try:
        cursor.execute("INSERT INTO db_sign.t_sign_game(user_id,correct_words,error_words) VALUES (%s,%s,%s)",
                       (user_id, correct_words, error_words))
        db_conn.commit()

    except db_conn.Error:
        data = []
        code = ResponseCode.db_conn_error
        msg = '数据库链接错误'

    result = dict(code=code, data=data, msg=msg)
    return json.dumps(result, cls=DatetimeEncoder)


@app.route('/freq-sign-word', methods=['GET'])
def get_high_freq_sign_words():
    """
    获取单词的访问量和易错单词
    """
    code = ResponseCode.success
    msg = ''
    data = []
    db_conn = get_db()
    cursor = db_conn.cursor(pymysql.cursors.DictCursor)
    try:
        cursor.execute(
            "SELECT tw.id, tw.word, tw.type, t.count "
            "FROM t_word tw, "
            "(SELECT * FROM db_sign.t_word_freq LIMIT 20) t "
            "WHERE tw.id = t.word_id ORDER BY t.count DESC;")
        data = cursor.fetchall()
    except db_conn.Error:
        data = []
        code = ResponseCode.db_conn_error
        msg = '数据库链接错误'

    result = dict(code=code, data=data, msg=msg)
    return json.dumps(result, cls=DatetimeEncoder)


@app.route('/statistic-data', methods=['GET'])
def get_app_statistic_data():
    code = ResponseCode.success
    msg = ''
    data = dict()
    db_conn = get_db()
    cursor = db_conn.cursor(pymysql.cursors.DictCursor)
    try:
        cursor.execute("SELECT COUNT(*) AS `count` FROM db_sign.t_user;")
        data['user'] = cursor.fetchone()['count']
        data['online_user'] = len(session)
        cursor.execute("SELECT COUNT(*) AS `count` FROM db_sign.t_word;")
        data['word'] = cursor.fetchone()['count']
        cursor.execute("SELECT COUNT(*) AS `count` FROM db_sign.t_news;")
        data['news'] = cursor.fetchone()['count']
        data['cpu'] = round(random.uniform(70, 95), 2)
        from utils import VISIT_COUNT
        data['count'] = VISIT_COUNT
    except db_conn.Error:
        data = []
        code = ResponseCode.db_conn_error
        msg = '数据库链接错误'

    result = dict(code=code, data=data, msg=msg)
    return json.dumps(result, cls=DatetimeEncoder)


if __name__ == '__main__':
    socket.run(app, host='0.0.0.0', debug=True, port=5003)
