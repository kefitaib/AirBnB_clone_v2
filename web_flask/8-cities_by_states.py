#!/usr/bin/python3
""" starts a Flask web application """


from flask import Flask
from models import storage
from models.state import State
app = Flask(__name__)


@app.teardown_appcontext
def teardown():
    """ close session """

    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def hello_world():
    """ function """

    s = storage.all(State)
    return render_template('8-cities_by_states.html', s=s)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
