"""This is the authentication blueprint constructor.
It creates the blueprint for authentication module.
"""
from flask import Blueprint

authentication = Blueprint('authentication', __name__)

from . import views