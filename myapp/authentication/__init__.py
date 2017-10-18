"""This is the authentication blueprint constructor.
It creates the blueprint for authentication module.
"""
from flask import Blueprint

authentication = Blueprint('auth', __name__)

from . import views