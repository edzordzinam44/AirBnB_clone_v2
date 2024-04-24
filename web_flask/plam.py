#!/usr/bin/python3
"""
start A Flask application
"""

from flask import Flask

# Create a Flask application instance
app = Flask(__name__)


# Define a route for the homepage
@app.route('/', strict_slashes=False)
def index():
    return 'Hello HBNB!'


# Define a route for /hbnb
@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'


# Define a route for /c/<text>
@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    return 'C ' + text.replace('_', ' ')


# Define a route for /python/<text>
@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    # Replace underscore (_) symbols with a space
    text = text.replace('_', ' ')
    return 'Python ' + text


# Define a route for /numberr/<n>
@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    return f'{n} is a number'


# Define a route for /number_template/<n>
@app.route('/number_template/<int:n>', strict_slashes=False)
def number_templates(n):
    return render_template('number_template.html', number=n)


# Run the Flask application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
