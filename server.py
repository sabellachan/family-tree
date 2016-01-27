"""Flask server file for family tree app."""

from jinja2 import StrictUndefined

from flask import Flask, render_template, redirect, request, flash, session, jsonify
from flask_debugtoolbar import DebugToolbarExtension

from model import User, Member, connect_to_db, db
import os
import uuid
import hashlib


app = Flask(__name__)

appkey = os.environ['appkey']

# Raise an error in Jinja2 if an undefined variable is used.
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def show_index():
    """Show homepage."""

    return render_template('index.html')


#############################################################################
# LOGIN


@app.route('/login')
def show_login():
    """Show login page."""

    if 'user' in session:
        flash('You are already logged in')

    return render_template('login.html')


#############################################################################
# HASH FUNCTIONS


def hash_password(password):
    """Hash and add a salt for a password."""

    salt = uuid.uuid4().hex
    return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt


def check_password(hashed_password, user_password):
    """Checks to see if the hashed password matches what a user enters to login."""

    password, salt = hashed_password.split(':')
    return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()


#############################################################################
# HELPER FUNCTIONS


if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the point
    # that we invoke the DebugToolbarExtension
    # app.debug = True

    connect_to_db(app)
    # connect_to_db(app, os.environ.get("DATABASE_URL"))

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    DEBUG = "NO_DEBUG" not in os.environ
    PORT = int(os.environ.get("PORT", 5000))

    app.run(host="0.0.0.0", port=PORT, debug=DEBUG)

    app.run()
