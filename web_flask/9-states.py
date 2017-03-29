#!/usr/bin/python3
"""
this module starts a Flask Web application
"""
from flask import Flask, render_template
from models import storage
app = Flask(__name__)


@app.route("/states", defaults={"id": ""}, strict_slashes=False)
@app.route("/states/<id>")
def states_hbnb(id):
    """
    route for /states/<id>

    returns all states if no id
    else returns all citys with the state

    """
    if id is "":
        obj = storage.all("State").values()
        return render_template("9-states.html",
                               state=id,
                               objs=obj)
    else:
        obj = storage.all("State")[id]
        state_name = obj.name
        list_cities = obj.cities
        return render_template("9-states.html",
                               state=state_name,
                               objs=list_cities)


@app.teardown_appcontext
def teardown_db(exception):
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
