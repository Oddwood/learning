from flask import Flask, render_template


app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')
app.config.from_pyfile('config.py')

from .models import User, Address
from .database import db, migrate

@app.route('/')
def index():
    return '<h1>Works!</h1>'

@app.route('/dbc')
def createDB():
    Address.query.delete()
    User.query.delete()
    
    addresses = []
    for i in range(10):
        addresses.append(Address(street="Freilager Nr." + str(i)))
    
    test = User(username="test_username", email="hello@user.ch", addresses=addresses)
    db.session.add(test)
    db.session.commit()
    
    return "Created used table"

@app.route('/users/')
def users():
    users = User.query.all()

    return render_template('user.html', users=users)