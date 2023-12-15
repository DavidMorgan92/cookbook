from flask import request, render_template, redirect, url_for, flash
from mongo import get_user_by_name_and_password, insert_user, user_exists
from routes.user.login_form import LoginForm
from routes.user.register_form import RegisterForm
from session import logout as logout_of_session, login as login_to_session


def register():
    """View func to register a new user."""

    form = RegisterForm()

    # If the form is posted and valid
    if form.validate_on_submit():
        if user_exists(form.username.data):
            # Flash a message if the username is taken
            flash("Username is already taken")
        else:
            # Create a user record in the database
            insert_result = insert_user(form.username.data, form.password.data)

            # Store the user ID in the session
            login_to_session(str(insert_result.inserted_id),
                             form.username.data)

            # Flash successful registered message
            flash(f"Welcome {form.username.data}")

            # Redirect to home page
            return redirect(url_for("home"))

    # Render the register template
    return render_template("user/register.html", form=form)


register.required_methods = ["GET", "POST"]


def login():
    """View func to log in the user."""

    form = LoginForm()

    # Get the redirect_url query parameter
    redirect_url = request.args.get("redirect_url", None)

    # If the form is posted and valid
    if form.validate_on_submit():
        # Get the user with the given username
        user = get_user_by_name_and_password(
            form.username.data, form.password.data)

        # If the username or password is incorrect
        if user == None:
            # Flash an error message
            flash("Username or password is incorrect")
        else:
            # Store the user ID in the session
            login_to_session(str(user["_id"]), user["name"])

            # Flash successful login message
            flash(f"Welcome {form.username.data}")

            # Redirect to the redirect_url if it is given
            if redirect_url:
                return redirect(redirect_url)

            # Redirect to home page
            return redirect(url_for("home_index"))

    # Render the login template
    return render_template("user/login.html", form=form, redirect_url=redirect_url)


login.required_methods = ["GET", "POST"]


def logout():
    """View func to log out the user."""

    # Clear the user stored in session
    logout_of_session()

    # Redirect to home page
    return redirect(url_for("home_index"))


logout.required_methods = ["POST"]
