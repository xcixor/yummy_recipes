"""This module imports the authentication blueprint.
It creates the routes for user authenication.
"""
from flask import render_template, redirect, request, url_for

from . import authentication

@authentication.route('/login', methods = ['GET', 'POST'])
def login():
    """Validates the User details and tries to Log the user in"""
    return render_template('authentication/login.html')

@authentication.route('/logout')
def logout():
    """Logs the user out"""
    return redirect(url_for('home.index'))
