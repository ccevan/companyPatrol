import os
from flask import Flask,request
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from werkzeug.utils import import_string
from config import config,baseconfig
from flask_moment import Moment
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from celery import Celery


mail = Mail()
moment = Moment()
db = SQLAlchemy()
csrf = CSRFProtect()
bootstrap = Bootstrap()

celery = Celery(__name__,backend=baseconfig.CELERY_RESULT_BACKEND,broker=baseconfig.CELERY_BROKER_URL)

def create_app(config_name):

    # 参加Flask应用程序实例
    app = Flask(__name__)
    config_mode = config[config_name]
    app.config.from_object(config_mode)
    db.init_app(app)
    csrf.init_app(app)
    moment.init_app(app)
    mail.init_app(app)
    bootstrap.init_app(app)
    celery.conf.update(app.config)
    filenames = os.listdir("app/resources")
    for filename in filenames:
        if os.path.isdir("app/resources/"+filename) and os.path.exists('app/resources/'+filename+'/__init__.py'):
            bp = import_string('app.resources.'+filename+':'+filename)
            app.register_blueprint(bp)
    return app,db


