"""Contains tests for the UserManager class"""

import sys

sys.path.append("..")

import unittest

from myapp.app_classes import User, UserManager

class TestUser(unittest.TestCase):
    """
    contains the test for a usermanager
    """
    def setUp(self):
        """Inititalizes the objects to test with"""
        self.user_mgr = UserManager()
        self.user_one = User("mike", "123456", "123456")
        self.user_two = User("alice", "al1234", "al1234")
        self.user_three = User("ptah", "123456", "78910")
        self.user_mgr.register_user(self.user_one)

    def tearDown(self):
        """Cleans up after objects have been used"""
        del self.user_mgr
        del self.user_one
        del self.user_two
        del self.user_three

    def test_register_user_twice(self):
        """Tests whether the app allows duplicate registration"""
        result = self.user_mgr.register_user(self.user_one)
        self.assertEqual(result, "User added registered")

    def test_passwords_match(self):
        """Tests whether passwords provided match"""
        result = self.user_mgr.register_user(self.user_three)
        self.assertEqual(result, "The passwords do not match")

    def test_user_login(self):
        """Tests whether its possible to log a registered user in"""
        self.user_mgr.register_user(self.user_two)
        result = self.user_mgr.login_user(self.user_two)
        self.assertEqual(result, "User successfully loged in")
        