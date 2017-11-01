"""This script runs the application"""

import unittest

from myapp import create_app

from flask_script import Manager

app = create_app('development')

manager = Manager(app)

@manager.command
def test():
    """Run the unit tests."""
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

if __name__ == '__main__':
    manager.run()
 