"""The purpose of this constructor is to set up the application
by importing the necessary modules for the app to run
Methods:
    create_app: Serves as the app factory
"""
from flask import Flask

from flask_bootstrap import Bootstrap

from config import config

from myapp.app_classes import User, Category, Recipe, Authentication

usr_mgr = Authentication()

myuser = User()

category = Category()

recipe = Recipe()

bootstrap = Bootstrap()


def create_app(configuration):
    """It initializes the application
    Args:
        configuration: The configuration to use for the application instance
    """

    app = Flask(__name__)
    app.config.from_object(config[configuration])
    config[configuration].init_app(app)

    bootstrap.init_app(app)

    from myapp.dashboard import dashboard as dashboard_blueprint
    app.register_blueprint(dashboard_blueprint, url_prefix='/dashboard')

    from myapp.authentication import authentication as authentication_blueprint
    app.register_blueprint(authentication_blueprint)

    return app


