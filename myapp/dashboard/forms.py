"""Creates the form for authentication"""

from flask_wtf import  FlaskForm

from wtforms import StringField, PasswordField, BooleanField, SubmitField

from wtforms.validators import Required, Email, Length, Email, Regexp, EqualTo

from wtforms import ValidationError

class RegistrationForm(FlaskForm):
    """
    The form class created the registration form
    """
    username = StringField('Username', render_kw={"placeholder": "username"}, \
            validators=[Required(), Length(2, 40)])
    email = StringField('Email', render_kw={"placeholder": "Email"}, \
            validators=[Required(), Length(1, 64), Email()])
    password = PasswordField('Password', render_kw={"placeholder": "password"}, \
            validators=[Required(), EqualTo('password2', message='Passwords must match.'), Length(6)])
    password2 = PasswordField('Confirm password', render_kw={"placeholder": "password"})
    submit = SubmitField('Register')

class CategoryForm(FlaskForm):
    """
    The form class creates the category management form
    """
    name = StringField('Name')
    description = StringField('Description')
    savesubmit = SubmitField('Save')
    exitsubmit = SubmitField('Exit')
    
class RecipeForm(FlaskForm):
    """
    This form class creates a Recipe management form
    """
    name = StringField('Name')
    ingredients = StringField('Ingredients')
    preparation = StringField('Preparation')
    savesubmit = SubmitField('Save')
    exitsubmit = SubmitField('Exit')
