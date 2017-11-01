"""Defines the classes for the application.
classes:
    User: This class instantiates a user to be added to the application
    Category: This class instantiates a category created by a user
    Recipe: Instantiates a recipe that belongs to a certain user's category
Methods:
"""
import re

class Authentication(object):
    """Manages the actions of the user and maintains a list of users who have registered."""
    def __init__(self):
        self.users = []

    def show_user(self, username):
        """Returns a list of all the items in the object's collection.
        Args:
            name(str): The name of the owning object.
        """
        registered_user = [user for user in self.users if user['username'] == username]
        return registered_user

    def register_user(self, user):
        """Checks the availability of the user in the user's collection
        and adds him if he doesn't exist.
        Args:
            user(object): The object of the user to add.
        """
        username = user.item_name
        password = user.pass_one
        confirm_password = user.pass_two
        email = user.user_email

        if self.show_user(username):
            return "User already registered"
        valid_password = self.validate_password(password)
        if valid_password:
            if password == confirm_password:
                valid_email = self.validate_email(email)
                if valid_email:
                    user = {'username':username, 'email':email, 'password':password}
                    self.users.append(user)
                    return "Registration successful"
                return "Invalid email"
            return "Passwords do not match"
        return self.validate_password(password)

    def validate_email(self, email):
        """Validates the email
        Args: email(str): The email to match
        """
        if re.match("^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$", email):
           return True
        return False

    def validate_password(self, password):
        """Validates the password
        Args(str): The password to match
        """
        if len(password) < 6:
            return False
        elif re.search('[0-9]', password) is None:
            return False
        elif re.search('[A-Z]', password) is None:
            return False
        return True

    def login_user(self, user):
        """Compares details provided with those on record to prove user's authenticity.
        Args:
            user(object): The user object to login.
        """
        username = user.item_name
        email = user.user_email
        password = user.pass_one

        registered_user = self.show_user(username)

        if registered_user:
            for user in registered_user:
                reg_email = user['email']
                reg_password = user['password']
                if email == reg_email and password == reg_password:
                    return "User successfully loged in"
                else:
                    return "Password/email combination is incorrect"
class AppObject(object):
    """Super class for objects with similar behavior in the app.
    Attributes:
        Name(str): Name of the object
    Methods:
        show_items: Returns a list of the items belonging to that object.
        find_item: Checks whether a certain item belongs to the particular object.
        add_item: Adds an item to that class.
        delete_item: Deletes an item from the containing collection.
        edit_item: Updates an item with new details provided.
    """
    def __init__(self, name):
        self.name = name
        self.items = []

    def show_items(self, owner):
        """Returns a list of all the items in the object's collection.
        Args:
            name(str): The name of the owning object
        """
        object_items = [item for item in self.items if item['owner'] == owner]
        return object_items
    def find_item(self, name, owner):
        """Checks whether a particular item belongs to a particular object's collection.
        Args:
            name(str): The name of the item to search for.
            owner(str): The name of the item whose collection is being searched.
        """
        object_items = self.show_items(owner)
        item_in_list = [item for item in object_items if item['name'] == name]
        if item_in_list:
            return True
    def add_item(self, item_to_add):
        """Adds an item to the main object's collection.
        Args:
            item_to_add(item): The item to be added to the collection.
        """
        pass

    def delete_item(self, name, owner):
        """Removes an item from the itemlist
        Args:
            name(str): the item's name that is used to remove the item's item.
        """
        for item in range(len(self.items)):
            if self.items[item]['name'] == name:
                del self.items[item]
                return self.show_items(owner)
        return None
    
    def edit_item(self, name, new_item):
        """Updates the details of the new item
        Args:
            name(str): contains the name of the item to edit.
            new_recipe(object): containes the details of the new recipe.
        """
        pass

class User(AppObject):
    """Inherits from AppObject and Instantiates a new user.
    Attributes:
        username(str): The user's name.
        password(str): The user's password.
        confirm_password(str): The user's confirmation password.
        email(str): The user's email
    Methods:
        add_item
        edit_item
    """
    def __init__(self, username="default user", password="default password", \
    confirm_password="default confirm password", email="defaultemail@email.com"):
        """initializes the attributes of the user created
        """
        super(User, self).__init__(name=username)
        self.password = password
        self.confirm_password = confirm_password
        self.email = email

    def get_name(self):
        """A getter for the name"""
        return self.name
    item_name = property(get_name)

    def get_pass_one(self):
        """A getter for the name"""
        return self.password
    pass_one = property(get_pass_one)

    def get_pass_two(self):
        """A getter for the name"""
        return self.confirm_password
    pass_two = property(get_pass_two)

    def get_email(self):
        """A getter for the email"""
        return self.email
    user_email = property(get_email)

    def add_item(self, category):
        """Creates category and adds it to the user's collection.
           Args:
               category(object): The category object to be added.
        """
        name = category.item_name
        owner = category.item_owner
        description = category.item_description

        if self.find_item(name, owner):
            return False
        category_toadd = {'name': name, 'description': description, 'owner': owner}
        self.items.append(category_toadd)
        return self.show_items(owner)


    def edit_item(self, name, new_category):
        """Updates the details of the new category.
        Args:
            name(str): contains the name of the category to edit.
            new_category(object): containes the details of the new category.
        """ 
        new_name = new_category.item_name
        owner = new_category.item_owner
        description = new_category.item_description

        category_to_edit = Category(new_name, description, owner)
        if self.find_item(name, owner):
            self.delete_item(name, owner)
            return self.add_item(category_to_edit)
        return False

class Category(AppObject):
    """Inherots from AppObject and creates a new category.
    Attributes:
            name(str): A name for the category.
            description(str): A short description about the category.
            owner(str): The user who created the category.
            recipes(object): A list of recipes belonging th the category.
    Methods:
            add_recipe: creates a recipe and adds it to the collection
            edit_recipe: updates the details of a recipe
            delete_recipe: removes a recipe from the collection
            show_recipe: returns a given category's recipes
            find_recipe: checks for the existence of a recip
    """
    def __init__(self, name="default category", description="default description", owner="default owner"):
        super(Category, self).__init__(name=name)
        self.description = description
        self.owner = owner

    def get_name(self):
        """A getter for the name"""
        return self.name
    item_name = property(get_name)

    def get_description(self):
        """A getter for the name"""
        return self.description
    item_description = property(get_description)

    def get_owner(self):
        """A getter for the owner"""
        return self.owner
    item_owner = property(get_owner)

    def add_item(self, recipe):
        """Creates a recipe and adds it to the category collection.
           Args:
               recipe(object): the object to add to the collection.
        """
        name = recipe.item_name
        owner = recipe.item_owner
        preparation = recipe.item_preparation
        ingredients = recipe.item_ingredients

        if self.find_item(name, owner):
            return False
        recipe_toadd = {'name': name, 'ingredients':ingredients, 'preparation': preparation, 'owner':owner}
        self.items.append(recipe_toadd)
        return self.show_items(owner)

    def edit_item(self, name, new_recipe):
        """Updates the details of the new recipe.
        Args:
            name(str): contains the name of the recipe to edit.
            new_recipe(object): containes the details of the new recipe.
        """       
        new_name = new_recipe.item_name
        owner = new_recipe.item_owner
        preparation = new_recipe.item_preparation
        ingredients = new_recipe.item_ingredients
        recipe_to_add = Recipe(new_name, ingredients, preparation, owner)
        if self.find_item(name, owner):
            self.delete_item(name, owner)
            return self.add_item(recipe_to_add)
        return False


class Recipe(object):
    """Creates a recipe
    Args:
        name(str): The name of the recipe created.
        ingredients(str): The requirements for the recipe.
        preparation(str): An explanation on how to prepare the meal.
        owner
    Methods:
    """

    def __init__(self, name="default recipe", ingredients="default ingredients", preparation="default preparation", owner="default owner"):
        """Initializes the attributes of the user created"""
        self.name = name
        self.ingredients = ingredients
        self.preparation = preparation
        self.owner = owner

    def get_name(self):
        """A getter for the name"""
        return self.name
    item_name = property(get_name)

    def get_ingredients(self):
        """A getter for the ingredients"""
        return self.ingredients
    item_ingredients = property(get_ingredients)

    def get_preparation(self):
        """A getter for the preparation"""
        return self.preparation
    item_preparation = property(get_preparation)

    def get_owner(self):
        """A getter for the owner"""
        return self.owner
    item_owner = property(get_owner)

    def __str__(self):
        return "Name: {0.item_name}, Ingredients: {0.item_ingredients}, Preparation: {0.item_preparation}".format(self)