from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!??</p>"

@app.route("/uniek")
def uniek():
    return "<p>Hello, Allemaal!</p>"

@app.route("/owes")
def owes():
    return "<p>Wij zijn het beste duo 100%</p>"