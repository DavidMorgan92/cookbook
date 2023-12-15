from flask_wtf import FlaskForm
from routes.user.form_fields import UsernameField, PasswordField


class RegisterForm(FlaskForm):
    """Register form model."""

    username = UsernameField()

    password = PasswordField()
