from flask import Flask
import socket, os

app = Flask(__name__)

@app.route("/")
def hello_world():
    html = f"<h1 style='color:{os.environ.get('FONT_COLOR')}'>{os.environ.get('CUSTOM_HEADER')}</h1>"
    return html