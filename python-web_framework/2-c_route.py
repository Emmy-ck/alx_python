"""Importing the flask web framework"""
from  flask import Flask

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

"""Check if the string is being executed directly and not imported"""

if __name__ == "__main__":
    """ Start the Flask development web server with debugging enabled."""
    app.run(debug=True)