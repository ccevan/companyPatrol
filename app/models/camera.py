from app import db
from datetime import datetime

class BaseModel(object):
    """模型基类，为每个模型补充创建时间与更新时间"""

    create_time = db.Column(db.DateTime, default=datetime.now)  # 记录的创建时间
    update_time = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)  # 记录的更新时间

class Camera(BaseModel,db.Model):
    __tablename__ = "camera"
    CameraId = db.Column(db.Integer, primary_key=True)
    CameraName = db.Column(db.String(64),unique=True,nullable=False)
    CameraIp = db.Column(db.String(32),nullable=False)
    CameraPort = db.Column(db.Integer,nullable=False)
    CameraAccount = db.Column(db.String(64))
    CameraPassWord = db.Column(db.String(32),nullable=False)
    CameraDesc = db.Column(db.String(128))
    CameraStatus = db.Column(db.Integer)

class Area(BaseModel,db.Model):
    __tablename__ = "area"
    AreaId = db.column(db.Integer,primery_key=True)
    AreaName = db.column(db.String(32))
    AreaDesc = db.Column(db.String(128))
    ParentId = db.Column(db.Integer)
    IsDelete = db.Column(db.Boolean)

    # camera = db.relationship("Camera",backref="area")



