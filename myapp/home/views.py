"""Contains the route for the landing page"""
from flask import render_template

from . import home

from flask import render_template, redirect, request, url_for, flash

from . import home

from .forms import Registration

from ..app_classes import User

@home.route('/')
def index():
    """Defines the landing page"""
    form = Registration()
    if form.validate_on_submit():
        user = User()
        if user.register_user(form.username.data, form.password.data, form.password2.data):
            flash('You can now login.')
            return render_template('dashboard/dashboard.html')
        return render_template('authentication/login.html')
    return render_template('index.html', form=form)

@home.route('/register', methods=['GET', 'POST'])
def register():
    form = Registration()
    if form.validate_on_submit():
        user = User()
        user.register_user(form.username.data, form.password.data, form.password2.data)
        flash('You can now login.')
        # return redirect(url_for('auth.login'))
        return render_template('home/index.html', form=form)
