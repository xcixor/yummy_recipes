"""Contains the route for the landing page"""

from . import home

from flask import render_template, request, redirect, session, url_for, flash

from . import home

from flask_login import login_user, logout_user, login_required, \
    current_user

from .. import myuser, recipe, category, usr_mgr

from .forms import RegistrationForm, CategoryCreation, CategoryEdit, RecipeCreation, RecipeEdit

@home.route('/dashboard')
@login_required
def dashboard():
    """Avails the user's dashboard"""
    user = session['username']
    mycategories = myuser.show_categories(user)
    return render_template('dashboard/dashboard.html', user_categories=mycategories)

@home.route('/', methods=['GET', 'POST'])
def index():
    """Defines the landing pae"""
    form = RegistrationForm()
    if form.validate_on_submit():
        username = form.username.data
        pass_1 = form.password.data
        pass_2 = form.password2.data
        if usr_mgr.register_user(username, pass_1, pass_2):
            session['username'] = username
            flash('You can now login.')
            return redirect(url_for('home.dashboard', form=form))
        flash("You cant login")
    return render_template('index.html', form=form)

@home.route('/create_category', methods=['GET','POST'])
def create_category():
    """Collects data about a category and creates a category"""
    user = session['username']
    form = CategoryCreation()
    if form.validate_on_submit():
        name = form.name.data
        description = form.description.data
        mycat = myuser.add_category(name, description, user)
        if isinstance(mycat, list):
            return render_template('/dashboard/dashboard.html', mycat=mycat)
        flash("Item already in list")
        return redirect(url_for('home.create_category', form=form))
    return render_template('dashboard/categoryadd.html', form=form)

@home.route('/logout')
def logout():
    """Logs the user out of the system"""
    session.pop('username', None)
    flash("You have been logged out")
    return redirect(url_for('home.index', form=RegistrationForm()))

@home.route('/edit_category/<name>', methods=['GET', 'POST'])
def edit_category(name):
    """Edits the category details"""
    user = session['username']
    categories = myuser.show_categories(user)
    old_name = ''
    old_description = ''
    for cat in categories:
        if cat['name'] == name:
            my_cat = cat
            old_name = my_cat['name']
            old_description = my_cat['description']
            break
    else:
        my_cat = None
        old_name = 'Not found'
        old_description = 'Not found'

    form = CategoryEdit()
    form.name.data = old_name
    form.description.data = old_description
    if form.validate_on_submit():
        new_name = request.form['name']
        new_description = request.form['description']
        mycat = myuser.edit_category(new_name, new_description, name, user)
        if isinstance(mycat, list):
            return render_template('/dashboard/dashboard.html', mycat=mycat)
    return render_template('dashboard/editcategory.html', form=form, name=old_name, description=old_description)

@home.route('/delete_category/<name>', methods=['GET', 'POST'])
def delete_category(name):
    """Deletes a category from the category list"""
    user = session['username']
    if myuser.delete_category(name):
        mycat = myuser.categories
        return render_template('/dashboard/dashboard.html', mycat=mycat)
    return render_template('/dashboard/dashboard.html')

@home.route('/create_recipe/<name>', methods=['GET','POST'])
def create_recipe(name):
    """Collects data about a category and creates a cateegory"""
    user = session['username']
    form = RecipeCreation()
    if form.validate_on_submit():
        rec_name = form.name.data
        description = form.description.data
        myrec = category.add_recipe(rec_name, description, name)
        if isinstance(myrec, list):
            return render_template('/dashboard/recipeview.html', myrec=myrec, owner=name)
        flash("Cannot add duplicate recipe")
    return render_template('/dashboard/addrecipe.html', form=form)

@home.route('/my_dash')
def my_dash():
    """Returns the user to the dashboard after working on recipes"""
    user = session['username']
    mycat = user.show_categories(user)
    return render_template('dashboard/dashboard.html', mycat=mycat)

@home.route('/delete_recipe/<name>/<owner>', methods=['GET', 'POST'])
def delete_recipe(name, owner):
    user = session['username']
    if category.delete_recipe(name):
        myrec = category.recipes
        return render_template('/dashboard/recipeview.html', myrec=myrec, owner=owner)
    render_template('/dashboard/recipeview.html')

@home.route('/edit_recipe/<name>/<owner>', methods=['GET', 'POST'])
def edit_recipe(name, owner):
    """Edits the details of the recipe"""
    user = session['username']
    recipes = category.show_recipes(owner)
    old_name = ''
    old_description = ''
    for a_recipe in recipes:
        if a_recipe['name'] == name:
            my_rec = a_recipe
            old_name = my_rec['name']
            old_description = my_rec['description']
            break
    else:
        my_rec = None
        old_name = 'Not found'
        old_description = 'Not found'

    form = RecipeEdit()
    form.name.data = old_name
    form.description.data = old_description
    if form.validate_on_submit():
        new_name = request.form['name']
        new_description = request.form['description']
        myrec = category.edit_recipe(new_name, new_description, old_name, owner)
        if isinstance(myrec, list):
            return render_template('/dashboard/recipeview.html', myrec=myrec, owner=owner)
    return render_template('dashboard/editrecipe.html', form=form, name=old_name, description=old_description)