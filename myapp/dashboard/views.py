"""Contains the route for the landing page"""

from myapp.dashboard import dashboard

from flask import render_template, request, redirect, session, url_for, flash

from myapp import myuser, category

from myapp import Category, Recipe

import sys

from myapp.dashboard.forms import CategoryForm, RecipeForm

@dashboard.route('/', methods=['GET','POST'])
def home():
    """Avails the user's dashboard"""
    user = session['username']
    mycategory = myuser.show_items(user)
    return render_template('dashboard/dashboard.html', mycategory=mycategory)

@dashboard.route('/create_category', methods=['GET','POST'])
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
            print(form.name.data)
            if name:
                cat_to_add = Category(name, description, owner)
                mycategory = myuser.add_item(cat_to_add)
                if isinstance(mycategory, list):
                    message = flash("Successfully added {} category".format(name))
                    return redirect(url_for('dashboard.home', mycategory=mycategory, message=message))
                flash("That item is already in the list")
                return redirect(url_for('dashboard.create_category', form=form))
            return redirect(url_for('dashboard.home', mycategory=myuser.show_items(owner), message=message))
        elif exit_btn:
            print('elif clicked')
            flash("No details provided for category")
            return redirect(url_for('dashboard.home'))
    return render_template('dashboard/categoryadd.html', form=form)

@dashboard.route('/edit_category/<name>', methods=['GET', 'POST'])
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
        mycategory = myuser.edit_item(old_name, edit_cat)
        if isinstance(mycategory, list):
            return render_template('/dashboard/dashboard.html', mycategory=mycategory)
    return render_template('dashboard/editcategory.html', form=form, name=old_name, description=old_description)

@dashboard.route('/delete_category/<name>', methods=['GET', 'POST'])
def delete_category(name):
    """Deletes a category from the category list"""
    owner = session['username']
    if myuser.delete_item(name, owner):
        mycategory = myuser.items
        return render_template('/dashboard/dashboard.html', mycategory=mycategory)
    return render_template('/dashboard/dashboard.html')

@dashboard.route('/create_recipe/<name>', methods=['GET','POST'])
def create_recipe(name):    
    """Collects data about a category and creates a cateegory"""
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
                myrecipe = category.add_item(rec_toadd)       
                if isinstance(myrecipe, list):
                    return render_template('/dashboard/recipeview.html', myrecipe=myrecipe, owner=name)  
                flash("That item is already in the list")
                return redirect(url_for('dashboard.create_recipe', form=form, name=name))
            flash("No details provided for new Recipe")
            return render_template('/dashboard/recipeview.html', myrecipe=category.show_items(name), owner=name)
        elif exit_btn:
            return render_template('/dashboard/recipeview.html', myrecipe=category.show_items(name), owner=name)
    return render_template('/dashboard/addrecipe.html', form=form)

@dashboard.route('/delete_recipe/<name>/<owner>', methods=['GET', 'POST'])
def delete_recipe(name, owner):
    """Deletes a recipe from the cateogory's list"""
    myrecipe = category.delete_item(name, owner)
    if isinstance(myrecipe, list):
        return render_template('/dashboard/recipeview.html', myrecipe=myrecipe, owner=owner)
    render_template('/dashboard/recipeview.html')

@dashboard.route('/view_recipes/<owner>', methods=['GET', 'POST'])
def view_recipes(owner):
    myrecipes = category.show_items(owner)
    if isinstance(myrecipes, list):
        return render_template('/dashboard/recipeview.html', myrecipe=myrecipes, owner=owner)
    render_template('/dashboard/recipeview.html')

@dashboard.route('/edit_recipe/<name>/<owner>', methods=['GET', 'POST'])
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
        myrecipe = category.edit_item(name, edited_rec)
        if isinstance(myrecipe, list):
            return render_template('/dashboard/recipeview.html', myrecipe=myrecipe, owner=owner)
    return render_template('dashboard/editrecipe.html', form=form, name=old_name, \
            ingredients=old_ingredients, preparation=old_preparation)

@dashboard.route('/view_all_recipes/<owner>', methods=['GET', 'POST'])
def view_all_recipes(owner):
    """View all the recipes belonging to particulat user"""
    pass
