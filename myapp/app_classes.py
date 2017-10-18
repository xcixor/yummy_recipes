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
        confirm_password(str): The user's confirmation password
    Methods:
        register_user: Adds a user to the user's collection
        login_user: Confirms the credentials of the user and grants access to account
    """
    def __init__(self):
        """adds a users to a collection of users
        Args:
        """
        self.users = []

    def register_user(self, username, password, confirm_password):
        """Checks the availability of the user in the user's collection
        and adds him if he doesn't exist
        """
        data = {}

        for a_user in self.users:
            if username == a_user['username']:
                return "User added already"
            else:
                if password != confirm_password:
                    return "The passwords do not match"

        data['username'] = username
        data['password'] = password
        self.users.append(data)
        return "registered successfuly!"

    def login_user(self, username, password):
        """Compares details provided with those on record to prove user's authenticity
        Args:
            username(str): user's name
            password
        """
        for a_user in self.users:
            if username == a_user['username'] and password == a_user['password']:
                return "User successfully loged in"
            else:
                return "Password/username combination is incorrect"

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

class Recipe(object):
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

def find_object(name, object_list):
    """Checks for the existence of an object in the list and returns if it exists,
    else it returns None
    Args:
        name(str): name of the object
        object_list(list(object)): the list to check for the item
    """
    for item in object_list:
        if item.name == name:
            return item
    return None