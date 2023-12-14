#!/usr/bin/python3
"""Starts a Flask web app
Listens to port 5000 on 0.0.0.0
"""
from models import storage
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """Displays HBNB filters on rendered page"""
    states = storage.all('State').values()
    amenities = storage.all('Amenity').values()
    return render_template('10-hbnb_filters.html', states=states, amenities=amenities)


@app.teardown_appcontext
def teardown(exception):
    """Remove session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
