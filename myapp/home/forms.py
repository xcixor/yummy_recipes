"""Creates the form for authentication"""

from flask_wtf import  FlaskForm

from wtforms import StringField, PasswordField, BooleanField, SubmitField

from wtforms.validators import Required, Email, Length, Email, Regexp, EqualTo

from wtforms import ValidationError

class RegistrationForm(FlaskForm):
    """TThe form class created the registration form"""
    username = StringField('Username', validators=[
        Required(), Length(1, 64)])
    password = PasswordField('Password', validators=[
        Required(), EqualTo('password2', message='Passwords must match.')])
    password2 = PasswordField('Confirm password', validators=[Required()])
    submit = SubmitField('Register')

class CategoryCreation(FlaskForm):
    """The form class creates the category creation form"""
    username = StringField('Username')
    description = StringField('Description')
    submit = SubmitField('Register')