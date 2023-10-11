"""Importing the flask web framework and render_template"""

from flask import Flask, render_template

"""Creating an instance of the Flask class and store it in the 'app' variable."""

app = Flask(__name__)

"""Defining a route for the root URL ('/') and associate it with the 'hello' function
"""

@app.route('/')
def hello():
    """ Return the string 'Hello HBNB!' as the response when the route is accessed."""

    return 'Hello HBNB!'

"""Defining a route for the hbnb URL and associate ti with the 'helloroute' function"""

@app.route('/hbnb')
def helloroute():
    """Return the string output as a response when this route is accessed"""
    return 'HBNB'

"""Defining a route for the c URL and associate it eith the 'disp_text' function with one argument 'text'"""

@app.route('/c/<text>')
def disp_text(text):
    """Replacing the _ with space if underscore is present in the route"""
    new_text = text.replace('_',' ')
    """Returns the concatnated new string without underscores"""
    return 'C ' + new_text

"""Defining a route for the python URL and associate it with the 'py_text' function."""
"""This dynamic route has a default text value"""
@app.route('/python/')
@app.route('/python/<text>')
def py_text(text='is cool'):
    """Replaces the underscore with a space"""
    new_text1 = text.replace('_',' ')
    """Returns the new string"""
    return 'Python ' + new_text1

"""Defining a route for the number URL and associating it with the 'num' function."""
@app.route('/number/<int:n>')
def num(n):
    """Converts int n into a string for the output"""
    m = str(n)
    """Displays a number only if the number is an integer."""
    return m + ' is a number'

"""Defining a new route for the number_template URL and associating it with the 'num_temp' function."""
@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """Displays the html page only if the number is an integer"""
    return render_template('5-number.html', number=n)

@app.route("/number_odd_or_even/<int:n>", strict_slashes = False)
def odd_or_even(n):
    return render_template('6-number_odd_or_even.html', number=n)

"""Check if the string is being executed directly and not imported"""

if __name__ == "__main__":
    """ Start the Flask development web server with debugging enabled."""
    app.run(host='0.0.0.0', port=5000)