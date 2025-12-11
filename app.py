from flask import Flask
from blueprints.general import app as general
from blueprints.admin import app as admin
from blueprints.user import app as user
import extentions 
import config

app=Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = config.SQLALCHEMY_DATABASE_URI
app.config['SECRET_KEY']=config.SECRET_KEY


app.register_blueprint(general)
app.register_blueprint(admin)
app.register_blueprint(user)
extentions.db.init_app(app)

with app.app_context():
  extentions.db.create_all()


if __name__=='__main__':
    app.run(debug=True, port=8080)