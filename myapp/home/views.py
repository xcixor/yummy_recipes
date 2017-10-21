"""Contains the route for the landing page"""
from flask import render_template

from . import home

from flask import render_template, redirect, session, url_for, flash

from . import home

from .. import user, recipe, category

from .forms import RegistrationForm, CategoryCreation

@home.route('/dashboard')
def dashboard():
    """Avails the user's dashboard"""
    user = session['username']
    categories = category.show_categories(user)
    form = CategoryCreation()
    # user = session['username']
    # if form.validate_on_submit():
    #     name = form.data.name
    #     description = form.data.description
    #     if category.add_category(name, description, user):
    #         flash("Category added successfully")
    #         # return render_template('dashboard/dashboard.html', form=form)
    #         return redirect(url_for('home.dashboard'))
    return render_template('dashboard/dashboard.html', user_categories = categories, form=form)

@home.route('/', methods=['GET', 'POST'])
def index():
    """Defines the landing page"""
    form = RegistrationForm()
    if form.validate_on_submit():
        username = form.username.data
        pass_1 = form.password.data
        pass_2 = form.password2.data
        if user.register_user(username, pass_1, pass_2):
            session['username'] = username
            flash('You can now login.')
            return redirect(url_for('home.dashboard', form=form))
        else:
            flash("You cant login")
        flash("You cant login")
    return render_template('index.html', form=form)



@home.route('/add_category', methods=['GET','POST'])
def add_category():
    user = session['username']
    form = CategoryCreation()
    if form.validate_on_submit():
        name = form.name.data
        description = form.description.data
        category.add_category(name,description,user)
        # return redirect(url_for('dashboard'))
        return render_template('dashboard/dashboard', form=form)

        


