from wtforms import StringField, PasswordField as WtfPasswordField, validators
import re


def UsernameField():
    """Generate a username field that can be used in multiple forms."""

    return StringField("Username", validators=[
        validators.DataRequired(),
        validators.Length(min=5, max=20),
        validators.Regexp("^[a-z0-9]{5,20}$", flags=re.IGNORECASE, message="Use only letters and numbers with no spaces")])


def PasswordField(label="Password"):
    """Generate a password field that can be used in multiple forms."""

    return WtfPasswordField(label, validators=[
        validators.DataRequired(),
        validators.Length(min=5)])
