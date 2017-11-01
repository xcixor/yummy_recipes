"""Creates forms for authentication"""

from flask_wtf import  FlaskForm

from wtforms import StringField, PasswordField, BooleanField, SubmitField

from wtforms.validators import Required, Email, Length, EqualTo

from wtforms import ValidationError

class LoginForm(FlaskForm):
    """
    This form class creates the login form
    """
    username = StringField('Username', validators=[Required(), Length(1, 64)])
    password = PasswordField('Password', validators=[Required()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log In')

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
