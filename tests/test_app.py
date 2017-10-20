import unittest

from flask import current_app

from myapp import create_app


class BasicsTestCase(unittest.TestCase):
    def setUp(self):
        """Creates the app"""
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_app_exists(self):
        """Tests if the app is created successfully"""
        self.assertFalse(current_app is None)
