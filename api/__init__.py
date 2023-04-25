# -*- coding: utf-8 -*-

"""初始化app
加载项目配置信息，创建全局flask实例
"""
from flask import Flask

from config import Config


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(Config)
    from dbconn import init_app
    init_app(app)
    return app
