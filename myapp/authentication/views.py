"""This module imports the authentication blueprint.
It creates the routes for user authenication.
"""
from flask import render_template, redirect, url_for, session, flash

from myapp.authentication import authentication

from myapp.authentication.forms import RegistrationForm, LoginForm

from myapp import User, usr_mgr

@authentication.route('/', methods=['GET', 'POST'])
def index():
    """Defines the landing page"""
    form = RegistrationForm()
    if form.validate_on_submit():
        username = form.username.data
        pass_1 = form.password.data
        pass_2 = form.password2.data
        usr = User(username, pass_1, pass_2)
        if usr_mgr.register_user(usr):
            session['username'] = username
            flash('You can now login.')
            return redirect(url_for('authentication.login', form=form))
        flash("Your password must have an alphabet digit combination")
    return render_template('index.html', form=form)

@authentication.route('/login', methods = ['GET', 'POST'])
def login():
    """Validates the User details and tries to Log the user in"""
    form = LoginForm()
    if form.validate_on_submit():
        # if session['logged_in']:
        #     return redirect(url_for('dashboard.home'))
        username = form.username.data
        password = form.password.data
        if usr_mgr.login_user(username, password):
            print('logged in')
            session['username'] = username
            return redirect(url_for('dashboard.home'))
        flash ('Check your credentials and try again')
    return render_template('authentication/login.html', form=form)

@authentication.route('/logout', methods = ['GET', 'POST'])
def logout():
    """Logs the user out of the system"""
    session.pop('username', None)
    flash("You have been logged out")
    return redirect(url_for('authentication.index', form=RegistrationForm()))


