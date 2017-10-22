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
        return True

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
    """Manages the addition, update, deletion and display of categories
    Methods:
        add_category: creates a category and adds it to the collection
        edit_category: updates the details of a category
        delete_category: removes the category fro the collection
        show_categories: returns a given user's categories
        find_category: checks for the existence of a category
    """

    def __init__(self):
        self.categories = []

    def show_categories(self, owner):
        user_categories = [category for category in self.categories if category['owner'] == owner]
        return user_categories

    def find_category(self, name, owner):
        user_categories = self.show_categories(owner)
        
        category_in_list = [category for category in user_categories if category['name'] == name]

        if category_in_list:
            return True
        

    def add_category(self, name, description, owner):
        """Areates a recipe category and adds it to the user collection
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
        """Remove a category from the list"""
        for category in range(len(self.categories)):
            if self.categories[category]['name'] == name:
                del self.categories[category]
                return "Deleted successfully"
            return "Category not exist"

    def edit_category(self, new_name,new_description, old_name, owner):
        """Updates the details of the new category
        Args:
            new_name(str): new name of category
            new_description(str): new description of category
        """
        if self.find_category(old_name, owner):
            self.delete_category(old_name)
            self.add_category(new_name, new_description, owner)
            return self.show_categories(owner)
        return "Item not exist"

class Recipe(object):
    """Manages the addition, update, deletion and display of recipes
    Methods:
        add_recipe: creates a recipe and adds it to the collection
        edit_recipe: updates the details of a recipe
        delete_recipe: removes the recipe fro the collection
        show_recipes: returns a given user's recipes
        find_recipe: checks for the existence of a recipe
    """

    def __init__(self):
        self.recipes = []

    def show_recipes(self, owner):
        """Returns a list of a user's recipes
        Args: the user whose recipes are to be returned
        """
        user_recipes = [recipe for recipe in self.recipes if recipe['owner'] == owner]
        return user_recipes

    def find_recipe(self, name, owner):
        """
        Checks for the existence of a recipe in a user's collection
        Args:
            name: recipe's name
            owner: the recipes owner
        """
        user_recipes = self.show_recipes(owner)
        
        recipe_in_list = [recipe for recipe in user_recipes if recipe['name'] == name]

        if recipe_in_list:
            return True
        

    def add_recipe(self, name, description, owner):
        """Creates a recipe recipe and adds it to the user collection
           Args:
               name(str): A name for the recipe
               description(str): A description of what it is
               owner(str): The name of the user who creates the recipe
        """
        if self.find_recipe(name,owner):
            return "Item alredy in list"
        recipe_toadd = {'owner': owner, 'name': name, 'description': description}
        self.recipes.append(recipe_toadd)
        return self.show_recipes(owner)
    
    def delete_recipe(self, name):
        """Remove a recipe from the list
        Args:
            name(str): name of recipes
        """
        for recipe in range(len(self.recipes)):
            if self.recipes[recipe]['name'] == name:
                del self.recipes[recipe]
                return "Deleted successfully"
            return "recipe not exist"

    def edit_recipe(self, new_name,new_description, old_name, owner):
        """Updates the details of the new recipe
        Args:
            new_name(str): new name of recipe
            new_description(str): new description of recipe
        """
        if self.find_recipe(old_name, owner):
            self.delete_recipe(old_name)
            self.add_recipe(new_name, new_description, owner)
            return self.show_recipes(owner)
        return "Item not exist"


