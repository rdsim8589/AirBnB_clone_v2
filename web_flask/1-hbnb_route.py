#!/usr/bin/python3
"""
this module starts a Flask Web application
"""
from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello_hbnb():
    """ route / will return 'Hello HBNB!' """
    return "Hello HBNB!"

@app.route("/hbnb")
def hbnb():
    """ /hbnb route returns HBNB"""
    return "HBNB"

if __name__ == "__main__":
    app.run(host="0.0.0.0")
