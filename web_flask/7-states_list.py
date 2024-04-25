#!/usr/bin/python3
"""
start flask application
"""


from flask import Flask, render_template
from models import *
from models import storage
app = Flask(__name__)


# Define route to display list of states
@app.route('/states_list', strict_slashes=False)
def states_list():
    # Retrieve states from storage and sort them alphabetically by name
    states = sorted(list(storage.all("State").values()), key=lambda x: x.name)
    return render_template('7-states_list.html', states=states)


# Define function to close storage connection on teardown
@app.teardown_appcontext
def teardown_db(exception):
    # Closes the storagee on teardown
    storage.close()


# Run Flask application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
