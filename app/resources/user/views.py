from . import user
from flask import render_template, redirect, url_for, request, sessions, make_response, abort
from datetime import datetime


@user.route('/')
def index():
    abort(404)
    return "hello"

@user.errorhandler(404)
def nofound(e):
    print("nodata")
    return render_template("user/error.html",current=datetime.utcnow()), 404

@user.route("/redirect")
def redirects():
    return redirect(url_for("user.index"))

@user.route("/hello/<string:name>/")
def helloindex(name):
    return "hello {}".format(name)


@user.route("/temp")
def template():
    return render_template("user/index.html", current_time = datetime.utcnow())













