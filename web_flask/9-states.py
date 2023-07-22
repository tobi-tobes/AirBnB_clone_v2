#!/usr/bin/python3
"""
9-states.py
This module contains a script that starts a Flask web application
"""

from flask import Flask, render_template
from markupsafe import escape
from models import storage
from models.state import State
from models.city import City
from os import getenv

app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def states():
    """display a HTML page"""
    states_dict = storage.all(State)
    states = sorted(states_dict.values(), key=lambda state: state.name)
    return render_template('9-states.html', states=states)


@app.route("/states/<id>", strict_slashes=False)
def states_id(id):
    """display a HTML page"""
    param = id
    states = storage.all(State)
    cities = []
    state = ""

    for key in states:
        state = states[key]
        if state.id == param:
            if getenv('HBNB_TYPE_STORAGE') == 'db':
                cities = state.cities
            else:
                cities = state.cities()
            cities = sorted(cities, key=lambda city: city.name)
            break

    return render_template('9-states.html', cities=cities, state=state)


@app.teardown_appcontext
def teardown_db(exception):
    """remove the current SQLAlchemy Session"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
