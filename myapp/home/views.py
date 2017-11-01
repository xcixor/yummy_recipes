"""Contains the route for the landing page"""

from . import home

from flask import render_template, request, redirect, session, url_for, flash

from . import home

from .. import myuser, category, usr_mgr, recipe

from .. import User, Category, Authentication, Recipe

from .forms import RegistrationForm, CategoryForm, RecipeForm

@home.route('/dashboard')
def dashboard():
    """Avails the user's dashboard"""
    user = session['username']
    mycategories = myuser.show_items(user)
    return render_template('dashboard/dashboard.html', user_categories=mycategories)

# @home.route('/', methods=['GET', 'POST'])
# def index():
#     """Defines the landing page"""
#     form = RegistrationForm()
#     if form.validate_on_submit():
#         username = form.username.data
#         pass_1 = form.password.data
#         pass_2 = form.password2.data
#         usr = User(username, pass_1, pass_2)
#         if usr_mgr.register_user(usr):
#             session['username'] = username
#             flash('You can now login.')
#             return redirect(url_for('home.dashboard', form=form))
#         flash("You cant login")
#     return render_template('index.html', form=form)

@home.route('/create_category', methods=['GET','POST'])
def create_category():
    """Collects data about a category and creates a category"""
    owner = session['username']
    form = CategoryForm()
    if form.validate_on_submit():
        save_btn  = form.savesubmit.data
        exit_btn = form.exitsubmit.data
        if save_btn:        
            name = form.name.data
            description = form.description.data
            if name:
                cat_to_add = Category(name, description, owner)
                mycat = myuser.add_item(cat_to_add)
                if isinstance(mycat, list):
                    message = flash("Successfully added {} category".format(name))
                    return render_template('/dashboard/dashboard.html', mycat=mycat, message=message)  
                flash("That item is already in the list")
                return redirect(url_for('home.create_category', form=form))
            flash("No details provided for new category")
            return render_template('/dashboard/dashboard.html', mycat=myuser.show_items(owner))
        elif exit_btn:
            mycat = myuser.show_items(owner)
            return render_template('/dashboard/dashboard.html', mycat=mycat)
    return render_template('dashboard/categoryadd.html', form=form)

# @home.route('/logout')
# def logout():
#     """Logs the user out of the system"""
#     session.pop('username', None)
#     flash("You have been logged out")
#     return redirect(url_for('home.index', form=RegistrationForm()))

@home.route('/edit_category/<name>', methods=['GET', 'POST'])
def edit_category(name):
    """Edits the category details"""
    owner = session['username']
    categories = myuser.show_items(owner)
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

    form = CategoryForm()
    form.name.data = old_name
    form.description.data = old_description
    if form.validate_on_submit():
        new_name = request.form['name']
        new_description = request.form['description']
        edit_cat = Category(new_name, new_description, owner)
        mycat = myuser.edit_item(old_name, edit_cat)
        if isinstance(mycat, list):
            return render_template('/dashboard/dashboard.html', mycat=mycat)
    return render_template('dashboard/editcategory.html', form=form, name=old_name, description=old_description)

@home.route('/delete_category/<name>', methods=['GET', 'POST'])
def delete_category(name):
    """Deletes a category from the category list"""
    owner = session['username']
    if myuser.delete_item(name, owner):
        mycat = myuser.items
        return render_template('/dashboard/dashboard.html', mycat=mycat)
    return render_template('/dashboard/dashboard.html')

@home.route('/create_recipe/<name>', methods=['GET','POST'])
def create_recipe(name):    
    """Collects data about a category and creates a cateegory"""
    # form = RecipeForm()
    # if form.validate_on_submit():
    #     rec_name = form.name.data
    #     ingredients = form.ingredients.data
    #     preparation = form.preparation.data
    #     rec_toadd = Recipe(rec_name, ingredients, preparation, name)
    #     myrec = category.add_item(rec_toadd)
    #     if isinstance(myrec, list):
    #         return render_template('/dashboard/recipeview.html', myrec=myrec, owner=name)
    #     flash("Cannot add duplicate recipe")
    # return render_template('/dashboard/addrecipe.html', form=form)
    # owner = session['username']
    form = RecipeForm()
    if form.validate_on_submit():
        save_btn  = form.savesubmit.data
        exit_btn = form.exitsubmit.data
        if save_btn: 
            rec_name = form.name.data
            ingredients = form.ingredients.data
            preparation = form.preparation.data
            if rec_name:
                rec_toadd = Recipe(rec_name, ingredients, preparation, name)
                myrec = category.add_item(rec_toadd)       
                if isinstance(myrec, list):
                    # message = flash("Successfully added {} recipe".format(rec_name))
                    return render_template('/dashboard/recipeview.html', myrec=myrec, owner=name)  
                flash("That item is already in the list")
                return redirect(url_for('home.create_recipe', form=form, name=name))
            flash("No details provided for new Recipe")
            return render_template('/dashboard/recipeview.html', myrec=category.show_items(name), owner=name)
        elif exit_btn:
            return render_template('/dashboard/recipeview.html', myrec=category.show_items(name), owner=name)
    return render_template('/dashboard/addrecipe.html', form=form)

@home.route('/my_dash')
def my_dash():
    """Returns the user to the dashboard after working on recipes"""
    user = session['username']
    mycat = myuser.show_items(user)
    return render_template('dashboard/dashboard.html', mycat=mycat)

@home.route('/delete_recipe/<name>/<owner>', methods=['GET', 'POST'])
def delete_recipe(name, owner):
    myrec = category.delete_item(name, owner)
    if isinstance(myrec, list):
        return render_template('/dashboard/recipeview.html', myrec=myrec, owner=owner)
    render_template('/dashboard/recipeview.html')

@home.route('/view_recipes/<owner>', methods=['GET', 'POST'])
def view_recipes(owner):
    myrecs = category.show_items(owner)
    if isinstance(myrecs, list):
        return render_template('/dashboard/recipeview.html', myrec=myrecs, owner=owner)
    render_template('/dashboard/recipeview.html')

@home.route('/edit_recipe/<name>/<owner>', methods=['GET', 'POST'])
def edit_recipe(name, owner):
    """Edits the details of the recipe"""
    recipes = category.show_items(owner)
    old_name = ''
    old_ingredients = ''
    old_preparation = ''
    for a_recipe in recipes:
        if a_recipe['name'] == name:
            my_rec = a_recipe
            old_name = my_rec['name']
            old_ingredients = my_rec['ingredients']
            old_preparation = my_rec ['preparation']
            break
    else:
        my_rec = None
        old_name = 'Not found'
        old_ingredients = 'Not found'
        old_preparation = 'Not found'
    form = RecipeForm()
    form.name.data = old_name
    form.ingredients.data = old_ingredients
    form.preparation.data = old_preparation
    if form.validate_on_submit():
        new_name = request.form['name']
        new_ingredients = request.form['ingredients']
        new_preparation = request.form['preparation']
        new_ingredients = request.form['ingredients']
        edited_rec = Recipe(new_name, new_ingredients, new_preparation, owner)
        myrec = category.edit_item(name, edited_rec)
        if isinstance(myrec, list):
            return render_template('/dashboard/recipeview.html', myrec=myrec, owner=owner)
    return render_template('dashboard/editrecipe.html', form=form, name=old_name, \
            ingredients=old_ingredients, preparation=old_preparation)

@home.route('/view_all_recipes/<owner>', methods=['GET', 'POST'])
def view_all_recipes(owner):
    """View all the recipes belonging to particulat user"""
    pass
