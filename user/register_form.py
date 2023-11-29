from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators
import re


class RegisterForm(FlaskForm):
    """Register form model."""

    username = StringField("Username", validators=[
        validators.DataRequired(),
        validators.Length(min=5, max=20),
        validators.Regexp("^[a-z0-9]{5,20}$", flags=re.IGNORECASE, message="Use only letters and numbers with no spaces")])

    password = PasswordField("Password", validators=[
        validators.DataRequired(),
        validators.Length(min=5)])
