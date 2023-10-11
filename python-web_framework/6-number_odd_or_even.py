#!/usr/bin/python3
"""
This is a script that directs a user to the home page of a site.
"""
from flask import Flask, render_template
from markupsafe import escape

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

@app.route('/c/<good>')
def display3(good):
    """
    This function returns the values of a dynamic route using flask!
    """
    good = good.replace('_', " ")
    return "C {}".format(escape(good))

@app.route('/python/<text>')
@app.route('/python/', defaults={'text': 'is_cool'})
def display4(text):
    """
    This function displays a default text.
    """
    text = text.replace('_', " ")
    return "Python {}".format(escape(text))

@app.route('/number/<int:n>')
def display5(n):
    return "{} is a number".format(n)

@app.route('/number_template/<int:n>')
def number_template(n):
    """Displays the HTML page only if the number is an integer"""
    try:
        return render_template('5.number.html', n=n)
    except Exception as e:
        print("Error", e)

@app.route('/number_odd_even/<int:n>')
def number_odd_or_even(n):
    """Displays the HTML page only depending on whether the number is odd or even"""
    if n % 2 == 0:
        m = str(n)
        return render_template('6.number_odd_or_even.html', n=m, odd_or_even='even')
    else:
        m = str(n)
        return render_template('6-number_odd_or_even.html', n=m, oddor_even='odd')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)