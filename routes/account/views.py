from flask import render_template, redirect, url_for, flash
from authorize import authorize
from session import logged_in_user_id
from routes.account.change_password_form import ChangePasswordForm
from mongo import update_user_password


@authorize
def index():
    """View func to show the logged in user's account options."""

    # Show the account index template with the logged in user's ID
    return render_template("account/index.html")


index.required_methods = ["GET"]


@authorize
def change_password():
    """View func to change the logged in user's password."""

    form = ChangePasswordForm()

    if form.validate_on_submit():
        result = update_user_password(
            logged_in_user_id(), form.old_password.data, form.new_password.data)

        if result != None:
            flash("Password changed")

            return redirect(url_for("account_index"))

        flash("Incorrect password")

    return render_template("account/change_password.html", form=form)


change_password.required_methods = ["GET", "POST"]
