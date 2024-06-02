from flask import Flask
import socket, os

app = Flask(__name__)

@app.route("/")
def hello_world():
    html = f"{os.environ.get('CUSTOM_HEADER')}</h1>"
    return html