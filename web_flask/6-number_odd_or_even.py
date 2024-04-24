#!/usr/bin/python3
"""
start Flask application
"""


from flask import Flask, render_template


# Create a Flask application instance
app = Flask(__name__)


# Define a route for the homepage
@app.route('/', strict_slashes=False)
def hello():
    return 'Hello HBNB!'


# Define a route for /hbnb
@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'


# Define a route for /c/<text>
@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    # Replace underscore (_) symbols with a space
    text = text.replace('_', ' ')
    return 'C ' + text


# Define a route for /python/<text>
@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    # Replace underscore (_) symbols with a space
    text = text.replace('_', ' ')
    return 'Python ' + text


# Define a route for /number/<n>
@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    return f'{n} is a number'


# Define a route foor /number_template/<n>
@app.route('/number_template/<int:n>', strict_slashes=False)
def numbersandtemplates(n):
    """display a HTML page only if n is an integer"""
    return render_template('5-number.html', n=n)


# Define a route for /number_odd_or_even/<n>
@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    odd_even = 'even' if n % 2 == 0 else 'odd'
    # Render the HTMl template with the given number and its odd/even
    return render_template('6-number_odd_or_even.html', n=n, odd_even=odd_even)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
