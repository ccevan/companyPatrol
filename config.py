import os

class baseconfig(object):
    DEBUG = True
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:{}@{}:3306/patrol'.format(
        os.environ.get("MYSQL_PASSWD",'mysql'),os.environ.get("MYSQL_HOST","127.0.0.1"))
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True

class mailconfig(baseconfig):
    NAME = "CHANGHAO"
    MAIL_SERVER = "smtp.163.com"
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    # MAIL_PASSWORD = os.environ.get('mail_password') 考虑安全性
    MAIL_DEFAULT_SENDER = 'flask<15890396381@163.com>'

config = {
    "baseconfig": baseconfig,
    "mailconfig": mailconfig,
}
