#!/usr/bin/python3
"""
this module starts a Flask Web application
"""
from flask import Flask, render_template
from models import storage
app = Flask(__name__)


@app.route("/states_list")
def states_list_hbnb():
    """
    route for /states_list

    returns the html of a list of states
    """
    return render_template("7-states_list.html", states=storage.all("State"))


@app.teardown_appcontext
def teardown_db(exception):
    """
    closes the the current sqlalchmeny session
    """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
