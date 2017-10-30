"""This file makes python treat the main directory as containing modules
It also defines the home blueprint
"""

from flask import Blueprint

home = Blueprint('home', __name__)

from . import views
