#!/usr/bin/python3
"""
Starts a Flask web app
"""


from flask import Flask, render_template
from models import *
from models import storage
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """
    renders HTML page with the states list
    """
    states = list(storage.all(State).values())
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown_db(exception):
    """
    closes the storage on teardown
    """
    storage.close()


if __name__ == '__main__':
    """
    run when invoked
    """
    app.run(host='0.0.0.0', port='5000')
