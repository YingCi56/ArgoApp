from flask import Flask
import socket, os

app = Flask(__name__)

@app.route("/")
def hello_world():
    html = f"<h1>{os.environ.get('CUSTOM_HEADER')}</h1><h2>Hey</h2>"
    return html