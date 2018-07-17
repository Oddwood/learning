from flask import Flask, render_template


app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')
app.config.from_pyfile('config.py')

from .models import User
from .database import db, migrate

@app.route('/')
def index():
    return '<h1>Works!</h1>'

@app.route('/dbc')
def createDB():
    User.query.delete()
    
    test = User(username="test_username", email="hello@user.ch", address="Test Address")
    test2 = User(username="test_username2", email="hello@user.ch2", address="Test Address2")
    db.session.add(test)
    db.session.add(test2)
    db.session.commit()
    
    return "Created used table"

@app.route('/users/')
def users():
    users = User.query.all()

    return render_template('user.html', users=users)