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

"""Check if the string is being executed directly and not imported"""

if __name__ == "__main__":
    """ Start the Flask development web server with debugging enabled."""
    app.run(debug=True)