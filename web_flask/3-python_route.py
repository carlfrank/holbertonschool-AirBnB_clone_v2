#!/usr/bin/python3
"""
Starts a Flask web app
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """returns hello at index"""
    return ("Hello HBNB!")


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """returns hbnb at hbnb"""
    return ('HBNB')


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """returns c will var value"""
    return "C " + text.replace('_', " ")


@app.route('/python', strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text='is cool'):
    """returns c will var value"""
    return "Python " + text.replace('_', " ")


if __name__ == "__main__":
    """run when invoked"""
    app.run(host='0.0.0.0', port='5000')
