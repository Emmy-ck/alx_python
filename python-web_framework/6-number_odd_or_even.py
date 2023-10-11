#!/usr/bin/python3
"""
This is a script that directs a user to the home page of a site.
"""
from flask import Flask, render_template

# Initialize the Flask module
app = Flask(__name__)

# Define the route for the root URL ('/')
@app.route("/", strict_slashes=False)
def main():
    """
    This function directs visitors to the homepage.
    """
    return "Hello HBNB!"

# Define the route for '/hbnb'
@app.route("/hbnb", strict_slashes=False)
def first():
    return "HBNB"

# Define the route for '/c/<text>'
@app.route("/c/<text>", strict_slashes=False)
def second(text):
    modified = "C " + text.replace('_', ' ')
    return modified

# Define the route for '/python/' and '/python/<text>'
@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def third(text="is cool"):
    modified = "Python " + text.replace('_', ' ')
    return modified

# Define the route for '/number/<n>'
@app.route("/number/<int:n>", strict_slashes=False)
def integer_check(n):
    return f"{n} is a number"

# Define the route for '/number_template/<n>'
@app.route("/number_template/<int:n>", strict_slashes=False)
def display_page(n):
    return render_template('5-number.html', number=n)

# Define the route for '/number_odd_or_even/<n>'
@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def odd_or_even(n):
    return render_template('6-number_odd_or_even.html', number=n)

if __name__ == "__main":
    app.run(host="0.0.0.0", port=5000)
    