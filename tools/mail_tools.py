
from app import mail
from flask_mail import Message
import os
from flask import current_app,render_template

def send_mail(to,subject,html_tem=None,txt_tem=None,accessory_path=None,**kwargs):
    msg = Message(
        subject=subject,
        sender=current_app.config.get("MAIL_DEFAULT_SENDER",None),
        recipients=[to]
    )
    # msg.body = "hello"
    msg.html = render_template(html_tem+".html",**kwargs)
    # msg.body = render_template(txt_tem+".txt")
    with current_app.open_resource(accessory_path) as fp:
        msg.attach(os.path.basename(accessory_path), "image/png", fp.read())
    mail.send(msg)

