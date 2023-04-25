# -*- coding: utf-8 -*-
"""
数据库连接
"""

import pymysql
from flask import current_app
from flask import g

from config import DBConfig


def get_db():
    """连接数据库"""
    server = DBConfig.SERVER
    port = DBConfig.PORT
    database = DBConfig.DATABASE
    user = DBConfig.USER
    password = DBConfig.PASSWORD
    if 'conn' not in g:
        conn = pymysql.connect(host=server,
                               port=port,
                               user=user,
                               password=password,
                               database=database)
        g.conn = conn
    return g.conn


def close_db(e=None):
    """关闭数据库连接"""
    conn = g.pop("conn", None)
    if conn is not None:
        conn.close()


def init_db():
    """初始化数据库，建立表结构"""
    conn = get_db()
    with current_app.open_resource("schema.sql") as f:
        conn.db.executemany(f.read().decode("utf-8"))


def init_app(app):
    """注册数据库操作函数,每次请求结束关闭数据库连接"""
    app.teardown_appcontext(close_db)
