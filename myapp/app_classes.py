"""Defines the classes for the application
classes:
    User: This class instantiates a user to be added to the application
    Category: This class instantiates a category created by a user
    Recipe: Instantiates a recipe that belongs to a certain user's category
Methods:
"""
class App(object):
    """Manages the actions of the user and maintains a list of users who have registered"""
    def __init__(self):
        self.users = []

    def register_user(self, username, password, confirm_password):
        """Checks the availability of the user in the user's collection
        and adds him if he doesn't exist
        Args:
            username(str): The name of the user to register
            password(str): The password of the user to register
            confirm_password(str): The confirmation password of the user to register
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
        return True

    def login_user(self, username, password):
        """Compares details provided with those on record to prove user's authenticity
        Args:
            username(str): The user to login name
            password(str): The user to login password
        """
        for a_user in self.users:
            if username == a_user['username'] and password == a_user['password']:
                return "User successfully loged in"
            else:
                return "Password/username combination is incorrect"

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
    def __init__(self, username, password, confirm_password):
        """initializes the attributes of the user created
        """
        self.username = username
        self.password = password
        self.confirm_password = confirm_password
        self.categories = []

    def show_categories(self, owner):
        """Shows a list of categories belonging to the user"""
        user_categories = [category for category in self.categories if category['owner'] == owner]
        return user_categories

    def find_category(self, name, owner):
        """Searches for a particular category belonging to the user"""
        user_categories = self.show_categories(owner)
        category_in_list = [category for category in user_categories if category['name'] == name]
        if category_in_list:
            return True
    def add_category(self, name, description, owner):
        """Creates category and adds it to the user's collection
           Args:
               name(str): A name for the category
               description(str): A description of what it is
               owner(str): The name of the user who creates the category
        """
        if self.find_category(name, owner):
            return "Item alredy in list"
        category_toadd = {'owner': owner, 'name': name, 'description': description}
        self.categories.append(category_toadd)
        return self.show_categories(owner)
    def delete_category(self, name):
        """Removes a category from the user's list
        Args:
            name(str): the category's name that is used to remove the category's object
        """
        for category in range(len(self.categories)):
            if self.categories[category]['name'] == name:
                del self.categories[category]
                return True
        return False

    def edit_category(self, new_name, new_description, old_name, owner):
        """Updates the details of the new category
        Args:
            new_name(str): new name of category
            new_description(str): new description of category
            old_name(str): The name to be replaced
            owner(str): The name of the object that owns the category
        """
        if self.find_category(old_name, owner):
            self.delete_category(old_name)
            self.add_category(new_name, new_description, owner)
            return self.show_categories(owner)
        return "Item not exist"

class Category(object):
    """Creates a new category
    Attributes:
            name(str): A name for the category
            description(str): A short description about the category
            owner(str): The user who created the category
            recipes(object): A list of recipes belonging th the category
    Methods:
            add_recipe: creates a recipe and adds it to the collection
            edit_recipe: updates the details of a recipe
            delete_recipe: removes a recipe from the collection
            show_recipe: returns a given category's recipes
            find_recipe: checks for the existence of a recipe
    """

    def __init__(self, name, description, owner):
        """Initializes the attributes of the class"""
        self.name = name
        self.description = description
        self.owner = owner
        self.recipes = []

    def get_name(self):
        """A getter for the name"""
        return self.name
    category_name = property(get_name)

    def show_recipes(self, owner):
        """Returns a list of recipes belonging to the category"""
        category_recipes = [recipe for recipe in self.recipes if recipe['owner'] == owner]
        return category_recipes

    def find_recipe(self, name, owner):
        """Checks whether a particular recipe belongs to a category"""
        category_recipes = self.show_recipes(owner)
        recipe_in_list = [recipe for recipe in category_recipes if recipe['name'] == name]
        if recipe_in_list:
            return recipe_in_list
    def add_recipe(self, recipe):
        """Creates a recipe and adds it to the category collection
           Args:
               name(str): A name for the recipe
               description(str): A description of what it is
               owner(str): The name of the category who creates the recipe
        """
        name = recipe.recipe_name
        owner = recipe.recipe_owner
        preparation = recipe.recipe_preparation
        ingredients = recipe.recipe_ingredients

        if self.find_recipe(name, owner):
            return False
        recipe_toadd = {'name': name, 'ingredients':ingredients, 'preparation': preparation, 'owner':owner}
        self.recipes.append(recipe_toadd)
        return self.show_recipes(owner)

    def delete_recipe(self, name):
        """Removes a recipe from the list
        Args:
            name(str): the recipe's name that is used to remove the recipe's object
        """
        for recipe in range(len(self.recipes)):
            if self.recipes[recipe]['name'] == name:
                del self.recipes[recipe]
                # return self.show_recipes(owner)
                return self.recipes
        return None

    def edit_recipe(self, name, new_recipe):
        """Updates the details of the new recipe
        Args:
            name(str): contains the name of the recipe to edit
            new_recipe(object): containes the details of the new recipe
        """       
        new_name = new_recipe.recipe_name
        owner = new_recipe.recipe_owner
        preparation = new_recipe.recipe_preparation
        ingredients = new_recipe.recipe_ingredients
        recipe_to_add = Recipe(new_name, ingredients, preparation, owner)
        if self.find_recipe(name, owner):
            self.delete_recipe(name)
            return self.add_recipe(recipe_to_add)
        return "False"

class Recipe(object):
    """Creates a recipe
    Args:
        name(str): The name of the recipe created
        description(str): A short description of the recipe created
        owner
    Methods:
    """

    def __init__(self, name, ingredients, preparation, owner):
        """Initializes the attributes of the user created"""
        self.name = name
        self.ingredients = ingredients
        self.preparation = preparation
        self.owner = owner

    def get_name(self):
        """A getter for the name"""
        return self.name
    recipe_name = property(get_name)

    def get_ingredients(self):
        """A getter for the ingredients"""
        return self.ingredients
    recipe_ingredients = property(get_ingredients)

    def get_preparation(self):
        """A getter for the preparation"""
        return self.preparation
    recipe_preparation = property(get_preparation)

    def get_owner(self):
        """A getter for the owner"""
        return self.owner
    recipe_owner = property(get_owner)
