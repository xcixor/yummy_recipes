"""Tests the Category class"""

import unittest

import sys

sys.path.append("..")

from myapp.app_classes import Category

class TestUser(unittest.TestCase):
    """contains the test for the category object methods
    """
    def setUp(self):
        """
        creates user objects for the tests
        """
        self.category = Category()
        

    def tearDown(self):
        """
        removes the objects after they have been used
        """
        del self.category

    def test_category_exist(self):
        """Tests the existence of a category"""
        self.category.add_category('Breakfast', 'Food for morning', 'ptah')
        result = self.category.add_category('Breakfast', 'Food for morning', 'ptah')
        self.assertEqual(result, "Item alredy in list")

    def test_delete_category(self):
        """Test if user deleted successfully"""
        self.category.add_category('Dessert', 'sweet food', 'ptah')
        result = self.category.delete_category('Dessert')
        self.assertEqual(result, "Deleted successfully")

    def test_edit_category(self):
        """Test if a category can be edited successfully"""
        self.category.add_category('Dessert', 'sweet food', 'ptah')
        result = self.category.edit_category('Brunch', 'Breakfast lunch combo', 'Dessert', 'ptah')
        self.assertEqual(result, self.category.categories)

    # def test_show_user_categories(self):
    #     self.category.add_category('Cousine', 'Dont know what that is', 'aly')
    #     result = self.category.show_categories('aly')
    #     self.assertEqual(result, True)

