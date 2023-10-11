#!/usr/bin/python3
"""
This is a script that directs a user to the home page of a site.
"""
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def display():
    """
    This function directs visitors to the homepage.
    """
    return "Hello HBNB!"

@app.route('/hbnb')
def display2():
    """
    This function directs visitors to the HBNB page.
    """
    return "HBNB"

@app.route('/c/<good>', strict_slashes=False)
def display3(good):
    """
    This function returns the values of a dynamic route using flask!
    """
    good = good.replace('_', " ")
    return "C {}".format((good))

@app.route('/python/<text>', strict_slashes=False)
@app.route('/python/', defaults={'text': 'is_cool'})
def display4(text):
    """
    This function displays a default text.
    """
    text = text.replace('_', " ")
    return "Python {}".format((text))

@app.route('/number/<int:n>', strict_slashes=False)
def display5(n):
    if isinstance(n, int):
        return "{} is a number".format(n)

@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """Displays the HTML page only if the number is an integer"""
    try:
        return render_template('6-number_odd_or_even.html', odd_or_even='even' if n % 2 == 0 else 'odd')
    except Exception as e:
        print("Error", e)

@app.route('/number_odd_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """Displays the HTML page only depending on whether the number is odd or even"""
    if n % 2 == 0:
        return render_template('6-number_odd_or_even.html', n=n, odd_or_even='even')
    else:
        return render_template('6-number_odd_or_even.html', n=n, odd_or_even='odd')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)