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

    def tearDown(self):
        del self.user_mgr
        del self.user_one
        del self.user_two
        del self.user_three

    def test_registrater_user(self):
        