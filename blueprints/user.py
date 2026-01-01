from flask import Blueprint,render_template,request,redirect,url_for,flash
from passlib.hash import sha256_crypt
from models.user import User
from extentions import db
from flask_login import login_user

app=Blueprint('user',__name__)

@app.route('/user/login',methods=['POST','GET'])
def login():
    if request.method=='GET':
        return render_template('user/login.html')
    else:
       register=request.form.get("register", None)
       username=request.form.get('username', None)
       password=request.form.get('password', None)
       phone=request.form.get('phone', None)
       address=request.form.get('address', None)

       if register != None:
          user=User.query.filter(User.username==username).first()
          if user!=None:
              flash(' please choose another username ')
              return redirect(url_for('user.login'))
          
          user= User(username=username,password=sha256_crypt.hash(password),phone=phone,address=address)
          db.session.add(user)
          db.session.commit()
          login_user(user)
          return redirect(url_for('user.dashboard'))
       
       else:
           user=User.query.filter(User.username==username).first()
           if user==None:
               flash(' username or password is wrong')
               return redirect(url_for('user.login'))
           if sha256_crypt.verify(password,user.password):
               login_user(user)
               return redirect(url_for('user.dashboard'))
           else:
               flash(' username or password is wrong')
               return redirect(url_for('user.login'))
           
       return "done"
    

@app.route('/user/dashboard',methods=['GET'])
def dashboard():
    return "dashboard"