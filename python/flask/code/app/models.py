from flask_sqlalchemy import SQLAlchemy
from .database import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    addresses = db.relationship('Address', backref='user', cascade="all, delete", lazy=True)

    def __repr__(self):
        return '<User %r>' % self.username

class Address(db.Model): 
    id = db.Column(db.Integer, primary_key=True)
    street = db.Column(db.String())

    person_id = db.Column(db.Integer, db.ForeignKey('user.id'))