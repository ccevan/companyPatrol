from app import db
from .camera import BaseModel


class User(BaseModel,db.Model):

    __tablename__ = "users"
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(64),unique=True,index=True)
    password = db.Column(db.String(64),nullable=True)
    email = db.Column(db.String(64),unique=True)
    role_id = db.Column(db.Integer,db.ForeignKey("roles.id"))

    def __repr__(self):
        return "<User {}>".format(self.username)

class Role(BaseModel,db.Model):

    __tablename__= "roles"
    id = db.Column(db.Integer,primary_key=True)
    rolename = db.Column(db.String(64),unique=True,index=True)
    users = db.relationship("User",backref="role",lazy="dynamic")

    def __repr__(self):
        return "<Role {}>".format(self.rolename)


