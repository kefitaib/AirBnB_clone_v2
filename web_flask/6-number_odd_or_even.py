#!/usr/bin/python3
""" starts a Flask web application """


from flask import Flask, render_template
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


@app.route('/number_template/<int:n>', strict_slashes=False)
def template(n):
    """ function """

    return render_template('5-number.html', n=n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def template_6(n):
    """ function """

    if n % 2 == 0:
        text = " is even"

    else:
        text = " is odd"

    return render_template('6-number_odd_or_even.html', n=n, text=text)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
