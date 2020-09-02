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

    text = text.replace('_', ' ')
    return 'C ' + text


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def display_Python(text='is cool'):
    """ function """

    text = text.replace('_', ' ')
    return 'Python ' + text


@app.route('/number/<int:n>', strict_slashes=False)
def is_number(n):
    """ function """

    return '{} is a number'.format(n)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
