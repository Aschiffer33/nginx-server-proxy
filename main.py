
import requests
from flask import Flask
import socket
import struct
app = Flask(__name__)

#change things to make it more pro like remove "get away spiders"

def ip():
    ip = get('https://api.ipify.org').text
    return ip
    




def updateduckdns(ip,ipv6):
    domain = 'domain'
    token = ''
    ipv6 = 'null'
    ipv4 = ip()
    URL = f"https://www.duckdns.org/update?domains={domain}&token={token}[&ip={ipv4}][&ipv6={ipv6}][&verbose=true][&clear=true]"
    requests.get(URL)



@app.route('/')
def index():
    return 'Hello worldeee!'




@app.route('/google')
def get_data():
      return requests.get('https://www.google.com/').content

app.config["DEBUG"] = false


@app.route('/', methods=['GET'])
def home():
    return "<h1>get away spiders</p>"


app.run()
