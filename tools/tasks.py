from celery import Celery
from flask import app

apps = Celery('companyPatrol.tools.tasks', backend="redis://:ch134197@39.107.107.0:6379/1", broker="redis://:ch134197@39.107.107.0:6379/0")

@apps.task
def sum(a,b):
    # with app.app_context():

    print(a+b)
    return a+b
