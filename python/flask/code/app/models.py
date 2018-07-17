from flask_sqlalchemy import SQLAlchemy
from .database import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    address = db.Column(db.String())

    def __repr__(self):
        return '<User %r>' % self.username