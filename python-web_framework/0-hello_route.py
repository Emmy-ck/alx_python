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

"""Check if the string is being executed directl and not imported"""

if __name__ == "__main__":
    """ Start the Flask development web server with debugging enabled."""
    app.run(debug=True)