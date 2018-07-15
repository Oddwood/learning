from flask import Flask

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')
app.config.from_pyfile('config.py')



from .views.user.user import user_view

app.register_blueprint(user_view)

@app.route("/")
def hello():
    return app.config.get('TEST')