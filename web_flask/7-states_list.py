#!/usr/bin/python3
""" starts a Flask web application """


from flask import Flask
from models import storage
app = Flask(__name__)


@app.teardown_appcontext
def teardown():
    """ close session """

    storage.close()


@app.route('/states_list', strict_slashes=False)
def hello_world():
    """ function """

    s = storage.all(State)
    return render_template('7-states_list.html', s=s)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
