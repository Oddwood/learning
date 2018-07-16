from flask import Flask
from flask_sqlalchemy import SQLAlchemy


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


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username


@app.route('/')
def index():
    return '<h1>man.</h1>'

@app.route('/dbc')
def createDB():
    User.query.delete()
    

    test = User(username="test_username", email="hello@user.ch")
    db.session.add(test)
    db.session.commit()

    return "Created used table"

@app.route('/users/')
def users():
    users = User.query.all()

    name = ''
    for user in users:
        name += user.username + " <b>::</b> "
    
    return name