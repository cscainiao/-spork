import os

import redis
from flask import Flask
from flask_session import Session

from App.house_views import house_blueprint
from App.models import db
from App.order_views import order_blueprint
from App.user_views import user_blueprint
from utils.setting import base_dir


def create_app():
    static_dir = os.path.join(base_dir, 'static')
    templates_dir = os.path.join(base_dir, 'templates')
    app = Flask(__name__, static_folder=static_dir, template_folder=templates_dir)
    app.register_blueprint(blueprint=user_blueprint, url_prefix='/user')
    app.register_blueprint(blueprint=house_blueprint, url_prefix='/house')
    app.register_blueprint(blueprint=order_blueprint, url_prefix='/order')

    app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:123456@10.7.152.57:3306/ihome"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    app.config['SECRET_KEY'] = 'secret_key'
    app.config['SESSION_TYPE'] = 'redis'
    app.config['SESSION_REDIS'] = redis.Redis(host='127.0.0.1', port=6379)

    # 初始化
    db.init_app(app=app)
    Session(app=app)

    return app
