"""The purpose of this constructor is to set up the application
by importing the necessary modules for the app to run
Methods:
    create_app: Serves as the app factory
"""
from flask import Flask

def create_app():
    """It initializes the application"""

    app = Flask(__name__)

    from .home import home as main_blueprint
    app.register_blueprint(main_blueprint)


    return app


