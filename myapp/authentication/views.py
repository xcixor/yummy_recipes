"""This module imports the authentication blueprint.
It creates the routes for user authenication.
"""
from flask import render_template, redirect, url_for, session

from . import authentication

from .forms import RegistrationForm

from .. import user

@authentication.route('/login', methods = ['GET', 'POST'])
def login():
    """Validates the User details and tries to Log the user in"""
    form = RegistrationForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        if user.login_user(username,password):
            session['username'] = username
            render_template('dashboard/dashboard.html')
    return render_template('authentication/login.html', form=form)


