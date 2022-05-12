from app import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))



class User:
    '''
    User class to define users
    '''

    def __init__(self,id,username,email,password,pitches,comments):
        self.id =id
        self.username = username
        self.email = email
        self.password = password
        self.pitches = pitches
        self.comments =comments

class Pitch:
    '''
    pitches class to define pitches
    '''

    def __init__(self,id,category,text,posted,comments):
        self.id =id
        self.category = category
        self.text= text
        self.posted = posted
        self.comments = comments


class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    password_hash = db.Column(db.String(255))


    def __repr__(self):
        return f'User {self.username}'

    pass_secure = db.Column(db.String(255))

@property
def password(self):
            raise AttributeError('You cannot read the password attribute')
@password.setter
def password(self, password):
            self.pass_secure = generate_password_hash(password)


def verify_password(self,password):
            return check_password_hash(self.pass_secure,password)

class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    users = db.relationship('User',backref = 'role',lazy="dynamic")


    def __repr__(self):
        return f'User {self.name}'