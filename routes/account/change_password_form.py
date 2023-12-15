from flask_wtf import FlaskForm
from routes.user.form_fields import PasswordField


class ChangePasswordForm(FlaskForm):
    old_password = PasswordField("Old Password")

    new_password = PasswordField("New Password")
