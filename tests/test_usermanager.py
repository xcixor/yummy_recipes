import sys

sys.path.append("..")

import unittest

from myapp.app_classes import User, UserManager

class TestUser(unittest.TestCase):
    """contains the test for a usermanager
    """
    def setUp(self):
        self.user_mgr = UserManager()
        self.user_one = User("mike", "123456", "123456")
        self.user_two = User("alice", "al1234", "al1234")
        self.user_three = User("ptah", "123456", "78910")
        self.user_mgr.register_user(self.user_one)

    def tearDown(self):
        del self.user_mgr
        del self.user_one
        del self.user_two
        del self.user_three

    def test_registrater_user_twice(self):
        result = self.user_mgr.register_user(self.user_one)
        self.assertEqual(result, "User added registered")

    def test_passwords_match(self):
        result = self.user_mgr.register_user(self.user_three)
        self.assertEqual(result, "The passwords do not match")

    def test_user_login(self):
        self.user_mgr.register_user(self.user_two)
        result = self.user_mgr.login_user(self.user_two)
        self.assertEqual(result, "User successfully loged in")
        