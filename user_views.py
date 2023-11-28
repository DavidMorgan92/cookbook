from flask import request, render_template, session, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from setup import mongo


def register():
    """View func to register a new user."""

    # If the form is posted
    if request.method == "POST":
        # Get the form values
        username = request.form.get("username")
        password = request.form.get("password")

        # See if there is already a user with this name
        user = mongo.db.users.find_one({"name": username})

        if user != None:
            # Flash a message if the username is taken
            flash("Username is already taken")
        else:
            # Create the user record
            user = {
                "name": username,
                "password_hash": generate_password_hash(password)
            }

            # Store the user record in the database
            insert_result = mongo.db.users.insert_one(user)

            # Store the user ID in the session
            session["user"] = {
                "id": str(insert_result.inserted_id)
            }

            # Flash successful registered message
            flash("Successfully registered")

            # Redirect to home page
            return redirect(url_for("home"))

    # Render the register template
    return render_template("user/register.html")


register.required_methods = ["GET", "POST"]


def login():
    """View func to log in the user."""

    # If the form is posted
    if request.method == "POST":
        # Get the form values
        username = request.form.get("username")
        password = request.form.get("password")

        # Get the user with the given username
        user = mongo.db.users.find_one({"name": username})

        # If the username or password is incorrect
        if user == None or not check_password_hash(user["password_hash"], password):
            # Flash a message
            flash("Username or password is incorrect")
        else:
            # Store the user ID in the session
            session["user"] = {
                "id": str(user["_id"])
            }

            # Flash successful login message
            flash("Successfully logged in")

            # Redirect to home page
            return redirect(url_for("home"))

    # Render the login template
    return render_template("user/login.html")


login.required_methods = ["GET", "POST"]


def logout():
    """View func to log out the user."""

    # Clear the user stored in session
    session["user"] = None

    # Redirect to home page
    return redirect(url_for("home"))


logout.required_methods = ["POST"]
