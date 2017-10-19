"""This module imports the authentication blueprint.
It creates the routes for user authenication.
"""
from flask import render_template, redirect, request, url_for, flash

from . import authentication

from .forms import RegistrationForm

from ..app_classes import User


@authentication.route('/login', methods = ['GET', 'POST'])
def login():
    """Validates the User details and tries to Log the user in"""
    return render_template('authentication/login.html')

@authentication.route('/logout')
def logout():
    """Logs the user out"""
    return redirect(url_for('home.index'))

@authentication.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    user = User()
    user.register_user(form.username.data, form.password, form.password2)
    flash('You can now login.')
    return render_template('dashboard/dashboard.html')
