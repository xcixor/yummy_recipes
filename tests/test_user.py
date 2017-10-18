"""Tests the User class"""

import unittest


from tests.app_classes import User

class TestUser(unittest.TestCase):
    """contains the test for the user object
    methods
    """
    def setUp(self):
        """
        creates user objects for the tests
        """
        self.user_1 = User('ptah', 'ptah123')
        self.user_2 = User('Alice', 'alibumaye')
        self.user_3 = User('James', 'Jamo')
        
        
        self.users = []

    def tearDown(self):
        """
        removes the objects after they have been user
        """
        pass

    def test_user_exist(self):
        """Tests whether the """
        self.assertEqual(self.user_1.name, 'ptah')
       