#!/usr/bin/python3
""" starts a Flask web application """


from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    """ function """

    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hello():
    """ function """

    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def display_C(text):
    """ function """

    return 'C ' + text

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
