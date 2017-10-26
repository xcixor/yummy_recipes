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
class AppObject(object):
    """Super class for objects with similar behavior in the app
    Attributes:
        Name(str): Name of the object
    Methods:
        show_items: Returns a list of the items belonging to that object
        find_item: Checks whether a certain item belongs to the particular object
        add_item: Adds an item to that class
        delete_item: Deletes an item from the containing collection
        edit_item: Updates an item with new details provided
    """
    def __init__(self, name):
        self.name = name
        self.items = []

    def show_items(self, owner):
        """Returns a list of all the items in the object's collection
        Args:
            name(str): The name of the owning object
        """
        object_items = [item for item in self.items if item['owner'] == owner]
        return object_items
    def find_item(self, name, owner):
        """Checks whether a particular item belongs to a particular object's collection
        Args:
            name(str): The name of the item to search for
            owner(str): The name of the item whose collection is being searched
        """
        object_items = self.show_items(owner)
        item_in_list = [item for item in object_items if item['name'] == name]
        if item_in_list:
            return True
    def add_item(self, item_to_add):
        """Adds an item to the main object's collection
        Args:
            item_to_add(item): The item to be added to the collection
        """
        pass

    def delete_item(self, name):
        """Removes an item from the itemlist
        Args:
            name(str): the item's name that is used to remove the item's item
        """
        for item in range(len(self.items)):
            if self.items[item]['name'] == name:
                del self.items[item]
                return self.items
        return None
    
    def edit_item(self, name, new_item):
        """Updates the details of the new item
        Args:
            name(str): contains the name of the item to edit
            new_recipe(object): containes the details of the new recipe
        """
        pass

class User(AppObject):
    """Inherits from AppObject and Instantiates a new user
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
        super(User, self).__init__(name=username)
        self.password = password
        self.confirm_password = confirm_password

    def add_item(self, category):
        """Creates category and adds it to the user's collection
           Args:
               name(str): A name for the category
               description(str): A description of what it is
               owner(str): The name of the user who creates the category
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
        """Updates the details of the new category
        Args:
            name(str): contains the name of the category to edit
            new_category(object): containes the details of the new category
        """ 
        new_name = new_category.item_name
        owner = new_category.item_owner
        description = new_category.item_description

        category_to_edit = Category(new_name, description, owner)
        if self.find_item(name, owner):
            self.delete_item(name)
            return self.add_item(category_to_edit)
        return False

class Category(AppObject):
    """Inherots from AppObject and creates a new category
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
            find_recipe: checks for the existence of a recip
    """
    def __init__(self, name, description, owner):
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
        """Creates a recipe and adds it to the category collection
           Args:
               name(str): A name for the recipe
               description(str): A description of what it is
               owner(str): The name of the category who creates the recipe
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
        """Updates the details of the new recipe
        Args:
            name(str): contains the name of the recipe to edit
            new_recipe(object): containes the details of the new recipe
        """       
        new_name = new_recipe.item_name
        owner = new_recipe.item_owner
        preparation = new_recipe.item_preparation
        ingredients = new_recipe.item_ingredients
        recipe_to_add = Recipe(new_name, ingredients, preparation, owner)
        if self.find_item(name, owner):
            self.delete_item(name)
            return self.add_item(recipe_to_add)
        return False


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