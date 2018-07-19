
from app import mail,celery
from flask_mail import Message
import os
from run import app
from flask import current_app,render_template



# celery = Celery('mail_tools', backend=current_app.config["CELERY_RESULT_BACKEND"], broker=current_app.config["CELERY_BROKER_URL"])

# @celery.task
# def send_async_mail(msg):
#     with app.app_context():
#         mail.send(msg)


@celery.task
def send_mail(to,subject,html_tem=None,accessory_path=None,**kwargs):
    with app.app_context():
        msg = Message(
            subject=subject,
            sender=current_app.config.get("MAIL_DEFAULT_SENDER",None),
            recipients=[to]
        )
        msg.html = render_template(html_tem+".html",**kwargs)
        # accessory_path 资源路径
        with current_app.open_resource(accessory_path) as fp:
            msg.attach(os.path.basename(accessory_path), "image/png", fp.read())

        mail.send(msg)


@celery.task
def sum(a,b):
    print(a+b)
    return a+b