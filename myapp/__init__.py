"""The purpose of this constructor is to set up the application
by importing the necessary modules for the app to run
Methods:
    create_app: Serves as the app factory
"""
from flask import Flask

from flask_bootstrap import Bootstrap

from config import config

bootstrap = Bootstrap()

def create_app(configuration):
    """It initializes the application"""

    app = Flask(__name__)
    app.config.from_object(config[configuration])
    config[configuration].init_app(app)

    bootstrap.init_app(app)

    from .home import home as main_blueprint
    app.register_blueprint(main_blueprint)

    from .authentication import authentication as authentication_blueprint
    app.register_blueprint(authentication_blueprint, url_prefix='/authentication')

    return app


