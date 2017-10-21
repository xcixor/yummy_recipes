"""This is the entry point for the main module"""

from flask import Blueprint

home = Blueprint('home', __name__)

from . import views
