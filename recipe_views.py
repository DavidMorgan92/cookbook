from flask import session, redirect, url_for, abort, render_template, request
from bson.objectid import ObjectId
from setup import mongo


def my_recipes():
    """
    Show a list of recipes belonging to the logged in user.
    """

    # Redirect to login if user is not logged in
    if session["user"] == None:
        return redirect(url_for("login"))

    # Get list of recipes belonging to the logged in user
    user_id = session["user"]["_id"]
    recipes = list(mongo.db.recipes.find({"creator": ObjectId(user_id)}))

    return render_template("my_recipes.html", recipes=recipes)


def edit_recipe(id):
    """
    Edit a recipe belonging to the logged in user.
    """

    # Redirect to login if user is not logged in
    if session["user"] == None:
        return redirect(url_for("login"))

    # Raise 404 error if the ID is invalid
    if not ObjectId.is_valid(id):
        abort(404)

    # Get the recipe with the given ID that also belongs to the logged in user
    user_id = session["user"]["_id"]
    recipe = mongo.db.recipes.find_one(
        {"_id": ObjectId(id), "creator": ObjectId(user_id)})

    # Raise 404 error if a matching recipe is not found
    if recipe == None:
        abort(404)

    return render_template("edit_recipe.html", recipe=recipe)


def delete_recipe(id):
    """
    Delete a recipe belonging to the logged in user.
    """

    # Redirect to login if the user is not logged in
    if session["user"] == None:
        return redirect(url_for("login"))

    # Raise 404 error if the ID is invalid
    if not ObjectId.is_valid(id):
        abort(404)

    user_id = session["user"]["_id"]

    if request.method == "POST":
        # Delete the recipe with the given ID that also belongs to the logged in user
        mongo.db.recipes.delete_one(
            {"_id": ObjectId(id), "creator": ObjectId(user_id)})
        
        return redirect(url_for("my_recipes"))

    # Get the recipe with the given ID that also belongs to the logged in user
    recipe = mongo.db.recipes.find_one(
        {"_id": ObjectId(id), "creator": ObjectId(user_id)})

    # Raise 404 error if a matching recipe is not found
    if recipe == None:
        abort(404)

    # Redirect user to my recipes page
    return render_template("delete_recipe.html", recipe=recipe)
