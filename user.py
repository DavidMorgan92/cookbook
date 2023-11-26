import re
from werkzeug.security import generate_password_hash, check_password_hash
from exceptions import UserAlreadyExists, InvalidUsername, InvalidPassword, UserDoesNotExist, IncorrectPassword


def create_user(mongo, username, password):
    """
    Creates a user in the database.
    Raises UserAlreadyExists if the username is taken.
    Raises InvalidUsername if the username is invalid.
    Raises InvalidPassword if the password is invalid.
    """

    # Raise exception if the username is already taken
    if get_user(mongo, username) != None:
        raise UserAlreadyExists

    # Raise exception if the username is invalid
    if not validate_username(username):
        raise InvalidUsername

    # Raise exception if the password is invalid
    if not validate_password(password):
        raise InvalidPassword

    # Create the user record to store in the database
    user = {
        "name": username,
        "password_hash": generate_password_hash(password)
    }

    # Insert the user record into the database
    mongo.db.users.insert_one(user)


def login_user(mongo, username, password):
    """
    Returns the user if it exists and the password is correct.
    Raises UserDoesNotExist if the username is not found.
    Raises IncorrectPassword if the password is incorrect.
    """

    # Get the user with the given username
    user = get_user(mongo, username)

    # Raise exception if the user doesn't exist
    if user == None:
        raise UserDoesNotExist

    # Raise exception if the password is invalid
    if not check_password_hash(user["password_hash"], password):
        raise IncorrectPassword

    return user


def get_user(mongo, username):
    """Returns the user object with the given username."""

    return mongo.db.users.find_one({"name": username})


def validate_username(username):
    """Returns True if the username is valid, otherwise False."""

    return re.fullmatch("^[a-zA-Z0-9]{5,15}$", username) != None


def validate_password(password):
    """Returns True if the password is valid, otherwise False."""

    return len(password) >= 6
