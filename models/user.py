from sqlalchemy import *
from extentions import db
from flask_login import UserMixin

class User(db.Model,UserMixin):
    __tablename__='users'
    id=Column(Integer,primary_key=True)
    username=Column(String(50),unique=True,nullable=False,index=True)
    password=Column(String(255),nullable=False,index=True)
    phone=Column(String(11),nullable=False,index=True)
    address=Column(String(255),nullable=False,index=True)
    #carts=db.relationship('Cart',back_populates='user')
