#!/usr/bin/python3
"""
Starts a Flask web application
"""


from flask import Flask, render_template
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Returns hello at index"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Returns hbnb at hbnb"""
    return 'HBNB'


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """Returns C and value"""
    return "C " + text.replace('_', ' ')


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text='is cool'):
    """Returns C and value"""
    return "Python " + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def num(n):
    """Displays n if its integer"""
    return "{:d} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def num_tem(n):
    """Renders template if its integer"""
    return render_template('5-number.html', n=n)


@app.route('number_odd_or_even/<int:n>', strict_slashes=False)
def odd_even(n):
    """Render template odd or even if integer"""
    if n % 2 == 0:
        even = 'even'
    else:
        even = 'odd'
    return render_template('6-number_odd_or_even.html', n=n, even=even)


if __name__ == "__main__":
    """run when invoked"""
    app.run(host='0.0.0.0', port='5000')
