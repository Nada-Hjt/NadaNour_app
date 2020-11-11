from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app=Flask(__name__)

app.config['SECRET_KEY']='thisismycloudificationproject'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///database/nourflask.db'
#app.config['SQLALCHEMY_DATABASE_URI']='postgresql://username:password@hostname:port/databasename'

db=SQLAlchemy(app)
bcrypt=Bcrypt(app)
login_manager=LoginManager(app)
from nour_flask import routes



