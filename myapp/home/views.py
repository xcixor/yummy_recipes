"""Contains the route for the landing page"""
from flask import render_template

from . import home

from flask import render_template, request, redirect, session, url_for, flash

from . import home

from .. import user, recipe, category

from .forms import RegistrationForm, CategoryCreation

@home.route('/dashboard')
def dashboard():
    """Avails the user's dashboard"""
    user = session['username']
    categories = category.show_categories(user)
    return render_template('dashboard/dashboard.html', user_categories = categories)

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



# @home.route('/add_category', methods=['GET','POST'])
# def add_category():
#     user = session['username']
#     form = CategoryCreation()
#     if request.method == 'POST':
#         name = form.name.data
#         description = form.description.data
#         category.add_category(name,description,user)
#         return redirect(url_for('dashboard'))
#     return render_template('index.html')

@home.route('/add_category')
def add_category():
    """Provides access to a form to create a category"""
    return render_template('dashboard/categoryadd.html')

@home.route('/create_category')
def add_category():
    """Collects data about a category and creates a cateegory"""
    user = session['username']
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        category.add_category(name,description,user)
        return redirect(url_for('dashboard'))
    return render_template('index.html')


        

