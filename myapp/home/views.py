"""Contains the route for the landing page"""
from flask import render_template

from . import home

from flask import render_template, request, redirect, session, url_for, flash

from . import home

# from .. import user, recipe, category, my_cat

from .. import recipe, category, user

from .forms import RegistrationForm, CategoryCreation, CategoryEdit, DeleteCategory, EditCategory

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
        mycat = category.add_category(name, description, user)
        return render_template('/dashboard/dashboard.html', mycat=mycat)
    return render_template('dashboard/categoryadd.html', form=form)

@home.route('/logout')
def logout():
    """Logs the user out of the system"""
    session.pop('username', None)
    return redirect(url_for('home.index', form=RegistrationForm()))

@home.route('/edit_category/<name>', methods=['GET', 'POST'])
def edit_category(name):
    """Edits the category details"""
    user = session['username']
    categories = category.show_categories(user)
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
        mycat = category.edit_category(new_name, new_description, name, user)
        return render_template('/dashboard/dashboard.html', mycat=mycat)
    return render_template('dashboard/editcategory.html', form=form, name=old_name, description=old_description)

@home.route('/delete_category/<name>', methods=['GET', 'POST'])
def delete_category(name):
    user = session['username']
    category.delete_category(name)
    mycat = category.categories
    return render_template('/dashboard/dashboard.html', mycat=mycat)






        

