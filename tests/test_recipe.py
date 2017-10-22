"""Tests the recipe class"""

import unittest

import sys

sys.path.append("..")

from myapp.app_classes import Recipe

class TestUser(unittest.TestCase):
    """contains the test for the Recipe object methods
    """
    def setUp(self):
        """
        creates user objects for the tests
        """
        self.recipe = Recipe()
        

    def tearDown(self):
        """
        removes the objects after they have been used
        """
        del self.recipe

    def test_recipe_exist(self):
        """Tests the existence of a recipe"""
        self.recipe.add_recipe('Breakfast', 'Food for morning', 'ptah')
        result = self.recipe.add_recipe('Breakfast', 'Food for morning', 'ptah')
        self.assertEqual(result, "Item alredy in list")

    def test_delete_recipe(self):
        
        """Test if user deleted successfully"""
        self.recipe.add_recipe('Dessert', 'sweet food', 'ptah')
        result = self.recipe.delete_recipe('Dessert')
        self.assertEqual(result, "Deleted successfully")

    def test_edit_recipe(self):
        self.recipe.add_recipe('Dessert', 'sweet food', 'ptah')
        result = self.recipe.edit_recipe('Brunch', 'Luch and breakfast combo', 'Dessert', 'ptah')
        self.assertEqual(result, self.recipe.recipes)

    # def test_show_user_categories(self):
    #     self.recipe.add_recipe('Cousine', 'Dont know what that is', 'aly')
    #     result = self.recipe.show_categories('aly')
    #     self.assertEqual(result, True)

