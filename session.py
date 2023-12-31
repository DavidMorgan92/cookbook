from flask import session


def is_logged_in():
    """Returns True if a user is logged in."""

    return "user" in session


def logged_in_user_id():
    """Gets the ID of the logged in user."""

    return session["user"]["id"]


def logged_in_user_name():
    """Gets the name of the logged in user."""

    return session["user"]["name"]


def context_processor():
    """Provides session data getters to all view templates."""

    return {
        "is_logged_in": is_logged_in,
        "logged_in_user_name": logged_in_user_name,
        "logged_in_user_id": logged_in_user_id
    }


def login(id, name):
    "Stores the user data in the session."

    session["user"] = {
        "id": id,
        "name": name
    }


def logout():
    "Clears the user data from the session."

    del session["user"]
