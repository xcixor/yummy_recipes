"""Tests the User class"""

import unittest

import sys

sys.path.append("..")

from myapp.app_classes import User

class TestUser(unittest.TestCase):
    """contains the test for the user object
    methods
    """
    def setUp(self):
        """
        creates user objects for the tests
        """
        self.user = User()
        
    def tearDown(self):
        """
        removes the objects after they have been used
        """
        del self.user
    def test_user_exist(self):
        """
        Test for the existence of a user in the list
        """

        self.user.users = [{'username' : 'peter', 'ptah' : 'ptah'}]
        result = self.user.register_user('peter', 'ptah', 'ptah')
        self.assertEqual(result, "User added already")

    def test_registration(self):
        """Checks whether user can register with correct details"""
        result = self.user.register_user('jim', 'ptah', 'ptah')
        self.assertEqual(result, True)

    def test_login(self):
        self.user.users = [{'username' : 'andela', 'password' : 'andela1'}]
        result = self.user.login_user('andela','andela1')
        self.assertEqual(result, "User successfully loged in")

# if __name__ == '__main__':
#     unittest.main