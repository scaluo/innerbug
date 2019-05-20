from datetime import datetime
from flask import current_app
from innerbug.extensions import db
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer,SignatureExpired,BadSignature

class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    loginname = db.Column(db.String(100),unique=True,index=True)
    password_hash = db.Column(db.String(128))
    username = db.Column(db.String(100))
    isadmin = db.Column(db.Boolean,default=False)
    bugs = db.relationship('Bug',back_populates='user')

    def set_password(self,password):
        self.password_hash = generate_password_hash(password)
        
    def check_password(self,password):
        return check_password_hash(self.password_hash,password)

    def rolename(self):
        if self.isadmin:
            return '管理员'
        else:
            return '操作员'

    def generate_auth_token(self, expiration = 3600):
        s = Serializer(current_app.config['SECRET_KEY'], expires_in = expiration)
        print(s)
        return s.dumps({ 'id': self.id }).decode('ascii')

    def to_json(self):
        dict = self.__dict__
        if "_sa_instance_state" in dict:
            del dict["_sa_instance_state"]
        return dict

    @staticmethod
    def verify_auth_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except SignatureExpired:
            return None # valid token, but expired
        except BadSignature:
            return None # invalid token
        user = User.query.get(data['id'])
        return user

class Project(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    projectname = db.Column(db.String(100),unique=True,index=True)
    ctime = db.Column(db.DateTime,default=datetime.utcnow)
    bugs = db.relationship('Bug',back_populates='project')

    def to_json(self):
        dict = self.__dict__
        if "_sa_instance_state" in dict:
            del dict["_sa_instance_state"]
        dict['ctime'] = self.ctime.strftime("%Y-%m-%d")
        return dict



class Bug(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(100))
    content = db.Column(db.Text)
    level = db.Column(db.String(10))
    ctime = db.Column(db.DateTime,default=datetime.utcnow)
    project_id = db.Column(db.Integer,db.ForeignKey('project.id'))
    project = db.relationship('Project',back_populates='bugs')
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    user = db.relationship('User',back_populates='bugs')    
    status = db.Column(db.Integer,default=0)
    otime = db.Column(db.DateTime,default=datetime.utcnow,onupdate=datetime.utcnow)
    def to_json(self):
        dict = self.__dict__
        if "_sa_instance_state" in dict:
            del dict["_sa_instance_state"]
        dict['ctime'] = self.ctime.strftime("%Y-%m-%d")
        return dict

def make_json(obj):
    dict = obj.__dict__
    if "_sa_instance_state" in dict:
        del dict["_sa_instance_state"]
    return dict    