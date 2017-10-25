"""Tests the Category class"""
import sys

sys.path.append("..")

import unittest

from myapp.app_classes import Category, Recipe


# from myapp import category


class TestUser(unittest.TestCase):
    """contains the test for the category object methods
    """
    def setUp(self):
        """
        creates a category object and two recipes and adds recipe_one to the category
        """
        self.category_one = Category("Soups", "Goes with other foods", "James")
        self.recipe_one = Recipe('Vegetable salad', 'corriander, vegetables', \
        'boil veggies and add corriander', 'Soups')
        self.category_one.add_recipe(self.recipe_one)
        self.recipe_two = Recipe("Beef stew", "beef, onions, pepper", \
        "Mix and boil in medium heat", "Soups")
        self.recipe_three = Recipe("Another recipe", "Some ingredients", \
        "A preparation", "Salads")
        
    def tearDown(self):
        """
        removes the objects after they have been used
        """
        del self.category_one
        del self.recipe_one
        del self.recipe_two
        del self.recipe_three

    def test_addrecipe(self):
        """Test whether a list of recipes is created when another is added"""
        result = self.category_one.add_recipe(self.recipe_two)
        self.assertEqual(result, [{'name': 'Vegetable salad', \
        'ingredients': 'corriander, vegetables', 'preparation': 'boil veggies and add corriander', 'owner' :'Soups'},\
        {'name': 'Beef stew', \
        'ingredients': 'beef, onions, pepper', 'preparation': 'Mix and boil in medium heat', 'owner': 'Soups'}])

    def test_recipe_exist(self):
        """Test whether the addition of an already existing recipe is not allowed"""
        result = self.category_one.add_recipe(self.recipe_one)
        self.assertEqual(result, False)
        
    def test_recipe_belongs_to_user(self):
        """Test whether the recipe in the category list belongs to that particular category only"""
        self.category_one.add_recipe(self.recipe_two)
        self.category_one.add_recipe(self.recipe_three)
        self.assertEqual(self.category_one.show_recipes('Soups'), [{'name': 'Vegetable salad', \
        'ingredients': 'corriander, vegetables', 'preparation': 'boil veggies and add corriander', 'owner' :'Soups'},\
        {'name': 'Beef stew', 'ingredients': 'beef, onions, pepper', 'preparation': 'Mix and boil in medium heat', 'owner': 'Soups'}])
        

    def test_delete_category(self):
        """Test if recipe deleted successfully"""
        self.category_one.add_recipe(self.recipe_two)
        result = self.category_one.delete_recipe('Beef stew')
        self.assertEqual(result,[{'name': 'Vegetable salad',\
        'ingredients': 'corriander, vegetables', 'preparation': 'boil veggies and add corriander', 'owner' :'Soups'}])  

    def test_edit_category(self):
        """Test if a category can be edited successfully"""
        new_recipe = self.recipe_two
        result = self.category_one.edit_recipe('Vegetable salad', new_recipe)
        self.assertEqual(result,[{'name': 'Beef stew', 'ingredients': 'beef, onions, pepper', \
        'preparation': 'Mix and boil in medium heat', 'owner': 'Soups'}])  

    def test_show_user_recipes(self):
        """Returns all the recipes of the category"""
        self.category_one.add_recipe(self.recipe_two)
        self.category_one.add_recipe(self.recipe_three)
        result = self.category_one.show_recipes(self.category_one.name)
        self.assertEqual(result, [{'name': 'Vegetable salad', \
        'ingredients': 'corriander, vegetables', 'preparation': 'boil veggies and add corriander', 'owner' :'Soups'},\
        {'name': 'Beef stew', \
        'ingredients': 'beef, onions, pepper', 'preparation': 'Mix and boil in medium heat', 'owner': 'Soups'}]))