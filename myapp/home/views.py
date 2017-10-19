"""Contains the route for the landing page"""
from flask import render_template

from . import home

@home.route('/')
def index():
    """Defines the landing page"""
    return render_template('index.html')

