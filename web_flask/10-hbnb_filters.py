#!/usr/bin/python3
"""
this module starts a Flask Web application
"""
from flask import Flask, render_template
from models import storage
app = Flask(__name__)


@app.route("/hbnb_filters/", strict_slashes=False)
def states_hbnb(id):
    """
    route for /hbnb_filters

    """
    states = storage.all("State").values()
    amenities = storage.all("Amenity").values()
    return render_template("10-hbnb_filters.html",
                               states=states,
                               amenities=amenity)


@app.teardown_appcontext
def teardown_db(exception):
    """
    teardown
    """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
