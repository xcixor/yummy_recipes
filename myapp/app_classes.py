"""Defines the classes for the application
classes:
    User: This class instantiates a user to be added to the applicatio
    Category: This class instantiates a category created by a user
    Recipe: Instantiates a recipe that belongs to a certain user's category
Methods:
"""

class User(object):
    """Instantiates a new user
    Attributes:
        username(str): The user's name
        password(str): The user's password
    Methods:
        add_category: adds a recipe_category to the user's collection
        show_categories: shows a list of the user's categories
        edit_category: edits a given recipe category
        delete_category: delete a given recipe category
    """
    def __init__(self, username, password):
        """creates a user instance
        Args:
            username(str): user's name
            password(str): user's password
        """
        self.username = username
        self.password = password
        self.categories = []

    def add_category(self, category):
        """Adds a recipe category to the user's collection
        Args:
            category (object): An object representing the shopping list to be added
        """
        self.categories.append(category)

    def show_categories(self):
        """Returns a list of the user's categories"""
        return self.categories
    def edit_shoppinglist(self):
        """Edits an existing shopping list in the user's collection"""
        pass
    def delete_shoppinglist(self, category):
        """Deletes an existing shopping list from the user's list"""
        self.categories.remove(category)
