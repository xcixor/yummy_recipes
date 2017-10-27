"""Tests the recipe class"""

import unittest

import sys

sys.path.append("..")

from myapp.app_classes import Recipe

class TestUser(unittest.TestCase):
    """
    contains the test for the Recipe object methods
    """
    def setUp(self):
        """Creates a recipe object for the tests"""
        self.recipe = Recipe()
        
    def tearDown(self):
        """Removes the objects after they have been used"""
        del self.recipe

    def test_recipe_exist(self):
        """Tests the existence of a recipe"""
        result = self.recipe.__str__()
        self.assertEqual(result, "Name: default recipe, Ingredients: default ingredients, Preparation: default preparation")
