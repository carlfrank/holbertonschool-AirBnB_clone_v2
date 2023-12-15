#!/usr/bin/python3
"""
Starts a Flask web app
"""


from flask import Flask, render_template
from models import storage, State
import sys

app = Flask(__name__)

@app.route('/states_list', strict_slashes=False)
def states_list():
    """
    Renders HTML page with the states list
    """
    try:
        states = list(storage.all(State).values())
        states.sort(key=lambda x: x.name)
        return render_template('7-states_list.html', states=states)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return "An error occurred", 500

@app.teardown_appcontext
def teardown_db(exception):
    """
    Closes the storage on teardown
    """
    storage.close()

if __name__ == '__main__':
    """
    Run when invoked
    """
    app.run(host='0.0.0.0', port=5000, debug=True)
