"""Creates the form for authentication"""

from flask_wtf import  FlaskForm

from wtforms import StringField, PasswordField, BooleanField, SubmitField

from wtforms.validators import Required, Email, Length, Email, Regexp, EqualTo

from wtforms import ValidationError

class RegistrationForm(FlaskForm):
    """
    The form class created the registration form
    """
    username = StringField('Username', render_kw={"placeholder": "username"}, validators=[
        Required(), Length(2, 40)])
    password = PasswordField('Password', render_kw={"placeholder": "password"}, validators=[
        Required(), EqualTo('password2', message='Passwords must match.'), Length(6)])
    password2 = PasswordField('Confirm password', render_kw={"placeholder": "password"}, validators=[Required()])
    submit = SubmitField('Register')

class CategoryForm(FlaskForm):
    """
    The form class creates the category management form
    """
    name = StringField('Name', validators=[Required()])
    description = StringField('Description')
    submit = SubmitField('Save')
    
class RecipeForm(FlaskForm):
    """
    This form class creates a Recipe management form
    """
    name = StringField('Name', validators=[Required()])
    ingredients = StringField('Ingredients')
    preparation = StringField('Preparation')
    submit = SubmitField('Save')
