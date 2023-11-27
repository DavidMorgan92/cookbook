from flask import request, render_template, session, redirect, url_for
from user import create_user, login_user
from exceptions import UserAlreadyExists, InvalidPassword, InvalidUsername, UserDoesNotExist, IncorrectPassword
from setup import mongo


def register():
    error = None

    if request.method == "POST":
        try:
            username = request.form.get("username")
            password = request.form.get("password")
            create_user(mongo, username, password)
        except UserAlreadyExists:
            error = "Username is already taken"
        except InvalidUsername:
            error = "Username is invalid"
        except InvalidPassword:
            error = "Password is invalid"
        else:
            return do_login(username, password)

    return render_template("register.html", error=error)


def login():
    error = None

    if request.method == "POST":
        try:
            username = request.form.get("username")
            password = request.form.get("password")
            return do_login(username, password)
        except (UserDoesNotExist, IncorrectPassword):
            error = "Username or password is incorrect"

    return render_template("login.html", error=error)


def logout():
    """
    Log out the user.
    Return a redirect to the home page.
    """

    session["user"] = None

    return redirect(url_for("home"))


def do_login(username, password):
    """
    Log the user in and store that in the session.
    Return a redirect to the home page.
    """

    user = login_user(mongo, username, password)

    session["user"] = {
        "_id": str(user["_id"]),
        "name": user["name"]
    }

    return redirect(url_for("home"))
