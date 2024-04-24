#!/usr/bin/python3
"""
start A Flask application
"""

from flask import Flask

# Create a Flask application instance
app = Flask(__name__)


# Define a route for the homepage
@app.route('/c/<text>', strict_slashes=False)
def index():
    return 'Hello HBNB!'


# Define a route for /hbnb
@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'


# Run the Flask application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
