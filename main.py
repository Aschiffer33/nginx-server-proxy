import requests
from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello world!'

    
@app.route('/some-url')
def get_data():
    return requests.get('https://www.google.com/').content





app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>get away spiders</p>"

app.run()

