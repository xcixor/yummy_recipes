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
            category (object): An object representing the category to be added
        """
        self.categories.append(category)

    def show_categories(self):
        """Returns a list of the user's categories"""
        return self.categories

    def edit_category(self):
        """Edits an existing category in the user's collection"""
        pass
    def delete_category(self, category):
        """Deletes an existing category from the user's list"""
        self.categories.remove(category)

class Category(object):
    """Creates a recipe category and adss recipes to it
    Attributes:
        name(str): A name for the category
        description(str): A description of what it is
    Methods:
        add_recipe: Adds a recipe to the category
        show_recipe: Returns a List with the category recipes
        edit_recipe: Edits an recipe in the category
        delete_recipe: Deletes an recipe in the category
    """

    def __init__(self, name, description):
        """Inititates a new category"""
        self.name = name
        self.description = description
        self.recipes = []

    def add_recipe(self, recipe):
        """Adds an recipe to the category
        Args:
            recipe(object): Represents the recipe to be added
        """
        self.recipes.append(recipe)
    def edit_category(self):
        """Changes the details of the category as provided by user"""
        pass

    def show_recipes(self):
        """Returns a list of the user's recipes"""
        return self.recipes

    def delete_recipe(self, recipe):
        """Deletes a recipe from the collection
        Args:
            recipe(object) The recipe to remove
        """
        self.recipes.remove(recipe)

class recipe(object):
    """Creates an Recipe to be added in the shopping list
    Attributes:
        name(str): The name of the recipe
        procedure(str): The method for preparing the meal
        servings(str): The number of servings it produces
        cost(str): The cost it takes to prepare the meal
    Methods:

    """
    def __init__(self, name, procedure, servings, cost):
        """Creates a recipe object"""
        self.name = name
        self.procedure = procedure
        self.servings = servings
        self.cost = cost