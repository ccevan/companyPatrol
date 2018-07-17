# coding=utf-8

from flask_migrate import Migrate, MigrateCommand
from flask_script import  Manager
from app import create_app
from app.models.camera import *

app, db = create_app("baseconfig")
manager = Manager(app)
migrate = Migrate(app, db)


# class Author(db.Model):
#     __tablename__ = 'authors'
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(64), unique=True)
#
#
#     def __repr__(self):
#         return 'Author:%s' % self.name


# manager是Flask-Script的实例，这条语句在flask-Script中添加一个db命令
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    print(app.url_map)
    manager.run()
