"""Contains the route for the landing page"""
from flask import render_template

from . import home

from flask import render_template, request, redirect, session, url_for, flash

from . import home

from .. import user, recipe, category

from .forms import RegistrationForm, CategoryCreation, CategoryEdit

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

@home.route('/create_category', methods=['GET','POST'])
def create_category():
    """Collects data about a category and creates a cateegory"""
    user = session['username']
    form = CategoryCreation()
    if form.validate_on_submit():
        name = form.name.data
        description = form.description.data
        mycat = category.add_category(name,description,user)
        return render_template('/dashboard/dashboard.html', mycat=mycat)
    return render_template('dashboard/categoryadd.html', form=form)

@home.route('/logout')
def logout():
    """Logs the user out of the system"""
    session.pop('username', None)
    return redirect(url_for('home.index', form=RegistrationForm()))

# @home.route('/edit_category', methods=['GET', 'POST'])
# def edit_category():
#     """Edits the category details"""
#     user = session['username']
#     categories = category.show_categories(user)
#     for items in categories:
#         old_name = categories['name']
#         old_description = categories['description']
#         form = CategoryEdit()
#         if form.validate_on_submit():
#             new_name = form.name.data
#             new_description = form.description.data
#             mycat = category.edit_category(new_name,new_description,old_name, user)
#             return redirect(url_for('home.dashboard', mycat=mycat))
#     return render_template('dashboard/editcategory.html',user, form=form)

@home.route('/edit_category', methods = ['GET','POST'])
def edit_category(name):
    """Edits the category details"""
    user = session['username']
    user_cats = category.show_categories(user)
    for the_category in user_cats:
        if the_category['name']==name:
            description = the_category['description']
    form = CategoryEdit()
    # if form.validate_on_submit():
    #     return render_template(url_for('dashboard/editcategories', user_cats))

    return render_template('dashboard/editcategory.html', name, description)



        

