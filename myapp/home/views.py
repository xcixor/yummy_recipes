"""Contains the route for the landing page"""
from flask import render_template

from . import home

from flask import render_template, redirect, session, url_for, flash

from . import home

from flask_login import login_user, logout_user, login_required

from .forms import Registration

from ..app_classes import User

@home.route('/')
def dashboard():
    """Avails the user's dashboard"""
    return render_template('dashboard/newdash.html')

@home.route('/', methods=['GET', 'POST'])
def index():
    """Defines the landing page"""
    form = Registration()
    if form.validate_on_submit():
        session['name'] = form.username.data
        user = User()
        if user.register_user(form.username.data, form.password.data, form.password2.data):
            # flash('You can now login.')
            return redirect(url_for('home.dashboard'))
    return render_template('index.html', form=form, name=session.get('name'))


