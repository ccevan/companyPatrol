from . import user
from flask_wtf import FlaskForm
from flask import session, request, make_response, g, current_app, render_template, url_for, redirect, flash
from wtforms import StringField, SubmitField, IntegerField, PasswordField,FileField
from wtforms.validators import EqualTo, Length,Email,DataRequired
from datetime import datetime
from app.models.UserModel import User, Role
from app.models.camera import Camera, Area
from app import db
import json
from tools import mail_tools
import os
from getRootPath import  RootPath

IMAGE_PATH = "/app/static/img/Avatar/"


class userForm(FlaskForm):
    name = StringField("user name", validators=[DataRequired(), Length(6, 12,
                                                                   message="the user name must be limited in 6-12 character")])
    password = PasswordField("password", validators=[DataRequired()])
    repassword = PasswordField("repassword", validators=[DataRequired(), EqualTo('password', message="两次密码输入必须一致")])
    email = StringField("email",validators=[DataRequired(),Email()])
    img = FileField("image",validators=[DataRequired()])
    submit = SubmitField()


@user.route("/login", methods=["POST", "GET"])
def login():
    name = None
    form = userForm()
    if form.validate_on_submit():
        # print(form.name.data)
        user = User.query.filter_by(username=form.name.data).first()

        filePath = RootPath()+IMAGE_PATH + form.img.data.filename
        with open(filePath,mode='wb') as f_write:
            f_write.write(form.img.data.read())

        if user is None:
            new_user = User(username=form.name.data,password=form.password.data,email=form.email.data)
            db.session.add(new_user)
            db.session.commit()
            session["known"] = False
            session["name"] = form.name.data
            mail_tools.send_mail(to=form.email.data,subject="flask",html_tem='mail_tem/html/welcome',txt_tem='mail_tem/txt/welcome',accessory_path=filePath,user=form.name.data)
            flash("successfully to sign up")
            # mail_tools.send_mail(to="2402779957@qq.com", subject="flask", html_tem='mail_tem/html/welcome',
            #                      txt_tem="mail_tem/txt/welcome", user=form.name.data)
        else:
            session["known"] = True
            flash("you had a account yet")
        return redirect(url_for("user.login"))
    return render_template("user/index.html",
                           name=session.get('name', "welcome to login"),
                           known=session.get("known", False),
                           form=form, current_time=datetime.utcnow())

    # old_name = session["name"]
    # new_name = form.name.data
    # if old_name is not None and old_name != new_name:
    #     flash("it seems like your name is changed!!!")
    #     s
    # name = form.name.data
    # session["name"] = name
    # form.name.data = ''
    # return redirect(url_for("user.login"))


@user.route("/findall")
def findall():
    users = User.query.all()
    print(users)
    # users = [user.username for user in users]
    users = [{"user_id": user.id, "user_name": user.username} for user in users]
    print(type(json.dumps(users)))
    data = {
        "return_id": 101,
        "users": users
    }
    return json.dumps(data)
#
# @user.route("/login/",methods=['POST','GET'])
# def login():
#
