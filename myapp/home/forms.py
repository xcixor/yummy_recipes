"""Creates the form for authentication"""

from flask_wtf import  FlaskForm

from wtforms import StringField, PasswordField, BooleanField, SubmitField

from wtforms.validators import Required, Email, Length, Email, Regexp, EqualTo

from wtforms import ValidationError

class RegistrationForm(FlaskForm):
    """TThe form class created the registration form"""
    username = StringField('Username', render_kw={"placeholder": "username"}, validators=[
        Required(), Length(2, 40)])
    password = PasswordField('Password', render_kw={"placeholder": "password"}, validators=[
        Required(), EqualTo('password2', message='Passwords must match.'), Length(8)])
    password2 = PasswordField('Confirm password', render_kw={"placeholder": "password"}, validators=[Required()])
    submit = SubmitField('Register')

class CategoryCreation(FlaskForm):
    """The form class creates the category creation form"""
    name = StringField('Name', validators=[Required()])
    description = StringField('Description')
    submit = SubmitField('Save')

class CategoryEdit(FlaskForm):
    """The form class creates the category editing form"""
    name = StringField('Name', validators=[Required()])
    description = StringField('Description')
    submit = SubmitField('Edit')
    
class RecipeCreation(FlaskForm):
    """The form class creates the recipe addition form"""
    name = StringField('Name', validators=[Required()])
    description = StringField('Description')
    submit = SubmitField('Save')

class RecipeEdit(FlaskForm):
    """The form class creates the recipe editing form"""
    name = StringField('Name', validators=[Required()])
    description = StringField('Description')
    submit = SubmitField('Edit')


