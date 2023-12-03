from flask import render_template, abort
from bson.objectid import ObjectId
from setup import mongo


def index(id):
    """View func to show a user's public profile."""

    # Raise 404 if id is invalid
    if not ObjectId.is_valid(id):
        abort(404)

    # Get the user with the given ID
    user = mongo.db.users.find_one({"_id": ObjectId(id)})

    # Raise 404 if the user is not found
    if user == None:
        abort(404)

    # Get the recipes belonging to the given user
    recipes = list(mongo.db.recipes.find({"creator": ObjectId(id)}))

    # Render the profile index template with the user's recipes and details
    return render_template("profile/index.html", recipes=recipes, user=user)


index.required_methods = ["GET"]
