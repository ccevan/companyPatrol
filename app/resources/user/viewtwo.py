from . import user
from flask_wtf import FlaskForm
from flask import session,request,make_response,g,current_app,render_template,url_for,redirect,flash
from wtforms import StringField,SubmitField,IntegerField,PasswordField
from wtforms.validators import required,EqualTo,Length
from datetime import datetime


class userForm(FlaskForm):
    name = StringField("user name",validators=[required(),Length(6,12,message="the user name must be limited in 6-12 character")])
    password = PasswordField("password",validators=[required()])
    repassword = PasswordField("repassword",validators=[required(),EqualTo('password',message="两次密码输入必须一致")])
    submit = SubmitField()

@user.route("/login",methods=["POST","GET"])
def login():
    name = None
    form = userForm()
    if form.validate_on_submit():
        old_name = session["name"]
        if old_name is not None and old_name != form.name.data:
            flash("it seems like your name is changed!!!")
        name = form.name.data
        session["name"] = name
        form.name.date = ''
        return redirect(url_for("user.login"))

    return render_template("user/index.html",name=session["name"],form=form,current_time=datetime.utcnow())
