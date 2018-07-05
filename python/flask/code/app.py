from flask import Flask, url_for
from utils.lister import Lister

app = Flask(__name__)

@app.route('/')
def index():
    
    listOfLinks = [
        'loop',
        'loop/15'
    ]
    
    linkList=''
    for links in listOfLinks:
        linkList += "<a href='{url}'>{link}</a><br />".format(url=links, link=links)


    return linkList

@app.route('/loop')
def loop():
    return "<ul>"+Lister.getList(5)+"</ul>"

@app.route('/loop/<int:numOfListElements>')
def loopofnum(numOfListElements: int) ->str:    
    if numOfListElements > 50:
        raise Exception("Input is too high")
    return "<ul>"+Lister.getList(numOfListElements)+"</ul>"