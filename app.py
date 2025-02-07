from flask import Flask
from zakaenjelle import huppakee

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!??</p>"

@app.route("/uniek")
def uniek():
    return "<p>Hello, Allemaal!</p>"

@app.route("/zakaenjelle")
def zakaenjelle():
    return huppakee()