from flask import request, render_template, session, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from exceptions import UserAlreadyExists, InvalidPassword, InvalidUsername, UserDoesNotExist, IncorrectPassword
from setup import mongo


def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if get_user(mongo, username) != None:
            flash("Username is already taken")
            return

        user = {
            "name": username,
            "password_hash": generate_password_hash(password)
        }

        mongo.db.users.insert_one(user)

        return login_user(username, password)

    return render_template("register.html")


def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        return login_user(username, password)

    return render_template("login.html")


def logout():
    """
    Log out the user.
    Return a redirect to the home page.
    """

    session["user"] = None

    return redirect(url_for("home"))


def login_user(username, password):
    """
    Log the user in and store that in the session.
    Return a redirect to the home page.
    """

    user = get_user(username)

    if user == None:
        flash("Username or password is incorrect")
        return

    if not check_password_hash(user["password_hash"], password):
        flash("Username or password is incorrect")
        return

    session["user"] = {
        "_id": str(user["_id"]),
        "name": user["name"]
    }

    return redirect(url_for("home"))


def get_user(username):
    """Returns the user object with the given username."""

    return mongo.db.users.find_one({"name": username})
