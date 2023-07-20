#!/usr/bin/python3
"""
3-python_route.py
This module contains a script that starts a Flask web application
"""

from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """display 'Hello HBNB!'"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """display 'HBNB'"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_is(text):
    """display 'C' followed by the value of the text variable"""
    param = escape(text)
    param = param.replace("_", " ")
    return "C {}".format(param)


@app.route("/python", defaults={'text': 'is_cool'}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_is(text):
    """display 'Python' followed by the value of the text variable"""
    param = escape(text)
    param = param.replace("_", " ")
    return "Python {}".format(param)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
