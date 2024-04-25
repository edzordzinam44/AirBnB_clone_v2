#!/usr/bin/python3
"""
Starts a Flask web application
"""

from flask import Flask, render_template
from models import *
from models import storage
app = Flask(__name__)


# Define a route to display the states and cities listed in order
@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    # Retrieve all state objects from storage
    states = storage.all("State").values()
    return render_template('8-cities_by_states.html', states=states)


# Define a function to close the storage connection on teardown
@app.teardown_appcontext
def teardown_db(exception):
    storage.close()


# Run the Flask application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
