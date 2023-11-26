import os
from flask import Flask, render_template, request, session, redirect, url_for
from flask_pymongo import PyMongo
from user import create_user, login_user
from exceptions import UserAlreadyExists, InvalidUsername, InvalidPassword, UserDoesNotExist, IncorrectPassword

# Initialize environment variables
try:
    import env
    env.initialize()
except:
    pass

# Create and configure Flask app and MongoDB connection
app = Flask("Cook Book")
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")
mongo = PyMongo(app)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/register", methods=["GET", "POST"])
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


@app.route("/login", methods=["GET", "POST"])
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


@app.route("/logout", methods=["POST"])
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


if __name__ == "__main__":
    host = "0.0.0.0"
    port = int(os.environ.get("PORT"))
    debug = os.environ.get("ENVIRONMENT") == "Development"
    app.run(host=host, port=port, debug=debug)
