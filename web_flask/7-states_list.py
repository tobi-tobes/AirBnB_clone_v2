#!/usr/bin/python3
"""
7-states_list.py
This module contains a script that starts a Flask web application
"""

from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    """display a HTML page"""
    states_dict = storage.all(State)
    states = sorted(states_dict.values(), key=lambda state: state.name)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown_db(exception):
    """remove the current SQLAlchemy Session"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
