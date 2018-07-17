from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')
app.config.from_pyfile('config.py')

app.config['SQLALCHEMY_DATABASE_URI'] = \
    'postgresql+psycopg2://{user}:{passwd}@{host}:{port}/{db}'.format(
        user=app.config['DBUSER'],
        passwd=app.config['DBPASS'],
        host=app.config['DBHOST'],
        port=app.config['DBPORT'],
        db=app.config['DBNAME']
    )
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True


db = SQLAlchemy(app)
migrate = Migrate(app, db)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    address = db.Column(db.String())

    def __repr__(self):
        return '<User %r>' % self.username


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