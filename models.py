import os
from flask_sqlalchemy import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
import json
from config import SQLALCHEMY_DATABASE_URI

db = SQLAlchemy()

def setup_db(app, database_path=SQLALCHEMY_DATABASE_URI):
    app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()

def db_drop_and_create_all():
    db.drop_all()
    db.create_all()



class Movies(db.Model):
    __tablename__ = 'Movies'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    release_date = db.Column(db.DateTime)

    def format(self):
        return {"title": self.title,
                "release_date": self.release_date}

class Actors(db.Model):
    __tablename__ = 'Actors'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    age = db.Column(db.Integer)
    gender = db.Column(db.String)