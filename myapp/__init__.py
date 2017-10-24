"""The purpose of this constructor is to set up the application
by importing the necessary modules for the app to run
Methods:
    create_app: Serves as the app factory
"""
from flask import Flask

from flask_bootstrap import Bootstrap

from flask_login import LoginManager

from config import config

from myapp import app_classes

usr_mgr = app_classes.App()

user = app_classes.User("default_user", "default_pass", "default_pass")

category = app_classes.Category("default_name", "default_description", "default_owner")

recipe = app_classes.Recipe("default_name", "default_description", "default_owner")

bootstrap = Bootstrap()

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'home.login'


def create_app(configuration):
    """It initializes the application"""

    app = Flask(__name__)
    app.config.from_object(config[configuration])
    config[configuration].init_app(app)

    bootstrap.init_app(app)
    login_manager.init_app(app)

    from .home import home as home_blueprint
    app.register_blueprint(home_blueprint)

    from .authentication import authentication as authentication_blueprint
    app.register_blueprint(authentication_blueprint, url_prefix='/authentication')

    return app


