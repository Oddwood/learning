from flask import Flask, request, redirect, url_for, render_template, flash
import requests as api_caller
import json

from utils.lister import Lister

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
def index():
    
    listOfLinks = [
        'loop',
        'loop/15',
        'users'
    ]

    return render_template('index.html', linkList=listOfLinks)

@app.route('/loop')
def loop():
    return redirect(url_for('loopofnum', numOfListElements=2))

@app.route('/loop/', defaults={'numOfListElements': None})
@app.route('/loop/<int:numOfListElements>')
def loopofnum(numOfListElements: int) ->str:
    
    if numOfListElements is None:
        numOfListElements=5

    if numOfListElements > 50:
        return "I see what you did there"
    
    return "<ul>"+Lister.getList(numOfListElements)+"</ul>"

@app.route('/users/')
def users():
    users = api_caller.get("https://jsonplaceholder.typicode.com/users/").json()
    return render_template('user.html', users=users, delmiter='---'*10)

@app.route('/users/<int:user_id>')
def user_profile(user_id):
    url = "https://jsonplaceholder.typicode.com/users/" + str(user_id)
    user = api_caller.get(url).json()

    if not user:
        flash("No Data available at " + request.full_path)
        return redirect(url_for('users'))


    out = """
        <h1>Hello {}</h1><br />
        <p>
           Your username is: {} 
        </p>
        <a href="/users">Go Back</a>
        
    """.format(user['name'], user['username'])

    return out