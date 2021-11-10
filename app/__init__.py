from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))

myobj = Flask(__name__) 

myobj.config.from_mapping(
                SECRET_KEY = 'you will know',SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir,'app.db'),SQLALCHEMY_TRACK_MODIFICATIONS = False,)

db = SQLAlchemy(myobj)

from app import route, models
