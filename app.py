from zakaenjelle import huppakee
from flask import Flask, render_template

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

@app.route("/wintersport")
def wintersport():
    return render_template("wintersport.html")

@app.route("/owes")
def owes():
    return "<p>Wij zijn het beste duo 100%</p>"
