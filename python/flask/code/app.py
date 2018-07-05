from flask import Flask, request, redirect, url_for
import requests as api_caller
import json

from utils.lister import Lister

app = Flask(__name__)

@app.route('/')
def index():
    
    listOfLinks = [
        'loop',
        'loop/15',
        'users'
    ]
    
    linkList=''
    for links in listOfLinks:
        linkList += "<a href='{url}'>{link}</a><br />".format(url=links, link=links)


    return linkList

@app.route('/loop')
def loop():
    return "<ul>"+Lister.getList(5)+"</ul>"

@app.route('/loop/', defaults={'numOfListElements': None})
@app.route('/loop/<int:numOfListElements>')
def loopofnum(numOfListElements: int) ->str:
    
    if numOfListElements is None:
        return redirect(url_for('loop'))

    if numOfListElements > 50:
        return "I see what you did there"
    
    return "<ul>"+Lister.getList(numOfListElements)+"</ul>"

@app.route('/users/')
def users():
    users = api_caller.get("https://jsonplaceholder.typicode.com/users/").json()

    out = ''
    for user in users:
        out += """
            name: {}<br />
            email: {}<br />
            adress: {}<br />
            website: <a href="http://www.{website}">{website}</a>
            <br /><br />
            <b>Profile: <a href="{path}{id}">View profile</a></b>
            <br /><br />
            {delmiter}
            <br />
        """.format(
            user['name'],
            user['email'],
            user['address']['city'],
            website = user['website'],
            id = user['id'],
            path = request.path,
            delmiter='---'*10 
        )

    return out

@app.route('/users/<int:user_id>')
def user_profile(user_id):
    url = "https://jsonplaceholder.typicode.com/users/" + str(user_id)
    user = api_caller.get(url).json()

    out = """
        <h1>Hello {}</h1><br />
        <p>
           Your username is: {} 
        </p>
        <a href="/users">Go Back</a>
        
    """.format(user['name'], user['username'])

    return out