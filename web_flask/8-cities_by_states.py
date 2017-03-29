#!/usr/bin/python3
"""
this module starts a Flask Web application
"""
from flask import Flask, render_template
from models import storage, state
app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states_hbnb():
    """
    route for /cities_by_states

    returns html of states and city
    """
    return render_template("8-cities_by_states.html",
                           states=storage.all("State"))


@app.teardown_appcontext
def teardown_db(exception):
    """
    removes the current mysql session
    """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
