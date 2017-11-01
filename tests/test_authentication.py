"""Contains tests for the UserManager class"""

import unittest

from myapp.app_classes import User, Authentication


class TestUser(unittest.TestCase):
    """
    contains the test for a usermanager
    """
    def setUp(self):
        """Inititalizes the objects to test with"""
        self.admin = Authentication()
        self.user_one = User("mike", "pN75216895", "pN75216895", "me@my.com")
        self.user_two = User("alice", "aW123456", "aW1234")
        self.user_three = User("ptah", "pn", "pn")

    def tearDown(self):
        """Cleans up after objects have been used"""
        del self.admin
        del self.user_one
        del self.user_two
        del self.user_three

    def test_register_user(self):
        """Test whether a user can be registered successfuly"""
        result = self.admin.register_user(self.user_one)
        self.assertEqual(result, "Registration successful")

    def test_register_user_twice(self):
        """Tests whether the app allows duplicate registration"""
        self.admin.register_user(self.user_one)
        result = self.admin.register_user(self.user_one)
        self.assertEqual(result, "User already registered")

    def test_passwords_match(self):
        """Tests whether passwords provided match"""
        result = self.admin.register_user(self.user_two)
        self.assertEqual(result, "Passwords do not match")

    def test_valid_password(self):
        """Tests the validity of a password"""
        result = self.admin.register_user(self.user_three)
        self.assertEqual(result, False)

    def test_user_login(self):
        """Tests whether its possible to log a registered user in"""
        self.admin.register_user(self.user_one)
        result = self.admin.login_user(self.user_one)
        self.assertEqual(result, "User successfully loged in")
        