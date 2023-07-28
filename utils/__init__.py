# -*- coding: utf-8 -*-
import base64
import json
import re
import uuid
from datetime import datetime, date
from flask import request

import oss2

from config import OSS

VISIT_COUNT = 0


def allow_cors(response):
    """
    允许跨域
    :param response:response
    :return: header中添加跨域支持
    """
    global VISIT_COUNT
    VISIT_COUNT = VISIT_COUNT + 1
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response


def response_json(response):
    """
    返回json格式的数据
    :param response: response
    :return: header中修改了Content-Type
    """
    if request.path.find("/assets") >= 0:
        return response
    if request.path != "/":
        response.headers['Content-Type'] = 'application/json'
    # response.headers['Content-Type'] = 'application/json'
    return response


def verify_phone(phone: str | int) -> bool:
    """
    验证手机号是否合法
    :param phone: 用户注册手机号
    :return: 格式合法的手机号返回true否则为false
    """
    ret = re.match(r"^1[35678]\d{9}$", str(phone))
    if ret:
        return True
    else:
        return False


def decode_base64(base64_data: str) -> str and bytes | None:
    """
    将base64字符串解码成二进制字节数组
    :param base64_data: base64字符串
    :return: 二进制字节数组
    """
    start_char = base64_data.find(':')
    end_char = base64_data.find(';')
    data_start_index = base64_data.find(',') + 1
    if start_char < 1 or end_char < 1:
        return None
    image_name = (base64_data[start_char + 1:end_char]).replace('/', '.')
    return image_name, base64.b64decode(base64_data[data_start_index:])


def upload_image(image: str | bytes | bytearray, image_name: str = "image.jpg") -> str:
    """
    上传图片到阿里云OSS
    :param image:
    :param image_name: 图片名，默认为image
    :return: 图片的URL
    """
    if type(image) is str:
        image_name, image = decode_base64(image)
    auth = oss2.Auth(OSS.AccessKeyId, OSS.AccessKeySecret)
    bucket = oss2.Bucket(auth=auth, endpoint=OSS.Endpoint, bucket_name=OSS.Bucket)
    key = 'images/' + str(str(uuid.uuid4().hex).replace('-', '') + '/' + image_name)
    bucket.put_object(key=key, data=image)
    image_url = 'https://' + OSS.Bucket + '.' + OSS.Endpoint + '/' + key
    return image_url.replace(' ', '')


def upload_file(file, file_name: str) -> str:
    """
    上传文件到OSS
    :param file: 文件
    :param file_name: 文件名
    :return: 访问文件的URL
    """
    auth = oss2.Auth(OSS.AccessKeyId, OSS.AccessKeySecret)
    bucket = oss2.Bucket(auth=auth, endpoint=OSS.Endpoint, bucket_name=OSS.Bucket)
    key = 'files/' + uuid.uuid4().hex.replace('-', '') + '/' + file_name
    bucket.put_object(key=key, data=file)
    file_url = 'https://' + OSS.Bucket + '.' + OSS.Endpoint + '/' + key
    return file_url


class DatetimeEncoder(json.JSONEncoder):
    def default(self, obj: any) -> any:
        """
        重写json构造类，增加对解析时间的支持
        """
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        else:
            return json.JSONEncoder.default(self, obj)


class ResponseCode:
    """
    response 状态码
    success 200 请求成功
    success_not_content 204 请求成功，响应数据与缓存中的一致
    param_missing 1001 参数缺失
    param_error 1002 参数解析错误
    db_conn_error 2001 数据库连接错误
    db_not_found 2002 数据库中不存在相应数据
    existed_error 3001 数据已存在于数据库中
    not_logged_in 4011 未登录
    """
    success = 200
    success_not_content = 204
    param_missing = 1001
    param_error = 1002
    db_conn_error = 2001
    db_not_found = 2002
    existed_error = 3001
    not_logged_in = 4011
