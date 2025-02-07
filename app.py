from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!??</p>"

@app.route("/uniek")
def uniek():
    return "<p>Hello, Allemaal!</p>"

@app.route("/wintersport")
def wintersport():
    return render_template("wintersport.html")

