#!/usr/bin/python3
"""
8-cities_by_states.py
This module contains a script that starts a Flask web application
"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
from collections import OrderedDict
from os import getenv

app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    """display a HTML page"""
    states_dict = storage.all(State)
    states = sorted(states_dict.values(), key=lambda state: state.name)
    state_cities = OrderedDict()
    storage_type = getenv('HBNB_TYPE_STORAGE')

    for state in states:
        if storage_type == 'db':
            cities = state.cities
        else:
            cities = state.cities()
        state_cities[state] = sorted(cities, key=lambda city: city.name)

    return render_template('8-cities_by_states.html',
                           state_cities=state_cities)


@app.teardown_appcontext
def teardown_db(exception):
    """remove the current SQLAlchemy Session"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
