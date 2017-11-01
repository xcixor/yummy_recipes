"""Tests the User class"""

import unittest

from myapp.app_classes import Category, User


class TestUser(unittest.TestCase):
    """
    contains the test for the category object methods
    """
    def setUp(self):
        """Creates a user object and three categories
        and adds category_one to the user's collection
        """
        self.user = User("ptah", "pN12345", "pN12345", "ptah@myemail.com")
        self.category_one = Category("Soups", "Goes with other foods", "ptah")
        self.category_two = Category("Main dishes", "Eaten for satisfaction", "ptah")
        self.category_three = Category("Salads", "gravy like dishes", "alice")
        self.user.add_item(self.category_one)
        
    def tearDown(self):
        """Removes the objects after they have been used"""
        del self.user
        del self.category_one
        del self.category_two
        del self.category_three

    def test_add_category(self):
        """Test whether a list of category items is created when several items are added"""
        result = self.user.add_item(self.category_two)
        self.assertEqual(result, [{'name': 'Soups', 'description': 'Goes with other foods', \
        'owner': 'ptah'}, {'name':'Main dishes', \
        'description': 'Eaten for satisfaction', 'owner': 'ptah'}])

    def test_category_exist(self):
        """Test whether the addition of an already existing category is not allowed"""
        result = self.user.add_item(self.category_one)
        self.assertEqual(result, True)
    
    def test_recipe_belongs_to_user(self):
        """Test whether the category in the user list belongs to that particular user only"""
        self.user.add_item(self.category_three)
        result = self.user.show_items('ptah')
        self.assertEqual(result, [{'name': 'Soups', 'description': 'Goes with other foods', \
        'owner': 'ptah'}])

    def test_delete_category(self):
        """Test if category is deleted successfully"""
        self.user.add_item(self.category_two)
        result = self.user.delete_item('Main dishes', self.user.name)
        self.assertEqual(result, [{'name': 'Soups', 'description': 'Goes with other foods', \
        'owner': 'ptah'}])

    def test_edit_category(self):
        """Test if a category can be edited successfully"""
        new_category = Category("Soups and extra", "Goes with other foods", "ptah")
        result = self.user.edit_item('Soups', new_category)
        self.assertEqual(result, [{'name': 'Soups and extra', 'description': 'Goes with other foods', \
        'owner': 'ptah'}])  

    def test_show_user_categories(self):
        """Returns all the categories of the user"""
        self.user.add_item(self.category_two)
        result = self.category_one.show_items(self.category_one.name)
        result = self.user.show_items(self.user.name)
        self.assertEqual(result, [{'name': 'Soups', 'description': 'Goes with other foods', \
        'owner': 'ptah'},\
        {'name':'Main dishes', 'description': 'Eaten for satisfaction', 'owner': 'ptah'}])
        