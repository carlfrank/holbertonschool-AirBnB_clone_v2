#!/usr/bin/python3
"""
Starts a Flask web app
"""
from models import storage
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states():
    """Display html template with list of states"""
    states = storage.all('State')
    return render_template('9-states.html', state=states)


@app.route('/states/<id>', strict_slashes=False)
def states_id(id):
    """Display html template with id info"""
    for state in storage.all('State').values():
        if state.id == id:
            return render_template('9-states.html', state=state)
    return render_template('9-states.html')


@app.teardown_appcontext
def teardown(exception):
    """remove session"""
    storage.close()


if __name__ == '__main__':
    """Run when invoked"""
    app.run(host='0.0.0.0', port='5000')
