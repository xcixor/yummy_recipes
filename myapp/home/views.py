"""Contains the route for the landing page"""
from flask import render_template

from . import home

from flask import render_template, redirect, session, url_for, flash

from . import home


from .forms import Registration

from ..app_classes import User

@home.route('/dashboard')
def dashboard():
    """Avails the user's dashboard"""
    return render_template('dashboard/dashboard.html')

@home.route('/', methods=['GET', 'POST'])
def index():
    """Defines the landing page"""
    form = Registration()
    if form.validate_on_submit():
        # session['name'] = form.username.data
        username = form.username.data
        pass_1 = form.password.data
        pass_2 = form.password2.data
        user = User()
        if user.register_user(username, pass_1, pass_2):
            session['username'] = username
            flash('You can now login.')
            return redirect(url_for('home.dashboard'))
        else:
            flash("You cant login")
        flash("You cant login")
    return render_template('index.html', form=form)

