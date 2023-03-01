from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField


class RegisterForm(FlaskForm):
    name = StringField('name')
    email = StringField('email')
    password = PasswordField('password')
    password_confirm = PasswordField('password2')

