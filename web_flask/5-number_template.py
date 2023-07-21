#!/usr/bin/python3
"""
5-number_template.py
This module contains a script that starts a Flask web application
"""

from flask import Flask, render_template
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


@app.route("/number/<int:n>", strict_slashes=False)
def n_is_a_number(n):
    """display 'n is a number' only if n is an integer"""
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """display an HTML page only if n is an integer"""
    return render_template('5-number.html', n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
