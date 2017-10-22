"""The purpose of this constructor is to set up the application
by importing the necessary modules for the app to run
Methods:
    create_app: Serves as the app factory
"""
from flask import Flask

from flask_bootstrap import Bootstrap

from config import config

from myapp import app_classes

from flask_wtf import CsrfProtect

user = app_classes.User()

category = app_classes.Category()

recipe = app_classes.Recipe()

bootstrap = Bootstrap()

csrf = CsrfProtect()


def create_app(configuration):
    """It initializes the application"""

    app = Flask(__name__)
    app.config.from_object(config[configuration])
    config[configuration].init_app(app)

    bootstrap.init_app(app)
    csrf.init_app(app)

    from .home import home as home_blueprint
    app.register_blueprint(home_blueprint)

    from .authentication import authentication as authentication_blueprint
    app.register_blueprint(authentication_blueprint, url_prefix='/authentication')

    return app


