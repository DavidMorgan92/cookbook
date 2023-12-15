from flask_wtf import FlaskForm
from routes.user.form_fields import UsernameField, PasswordField


class LoginForm(FlaskForm):
    """Login form model."""

    username = UsernameField()

    password = PasswordField()
