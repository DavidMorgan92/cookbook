from flask import session, redirect, url_for, abort, render_template, request, flash
from bson.objectid import ObjectId
from setup import mongo


def index():
    """View func to show a list of recipes belonging to the logged in user."""

    # Redirect to login if user is not logged in
    if session["user"] == None:
        return redirect(url_for("user/login"))

    # A filter to locate the logged in user's recipes in the database
    filter = {"creator": ObjectId(session["user"]["id"])}

    # Get list of recipes belonging to the logged in user
    recipes = list(mongo.db.recipes.find(filter))

    # Render template with list of recipes
    return render_template("recipes/index.html", recipes=recipes)


index.required_methods = ["GET"]


def edit(id):
    """View func to edit a recipe belonging to the logged in user."""

    # Redirect to login if user is not logged in
    if session["user"] == None:
        return redirect(url_for("user/login"))

    # Raise 404 error if the ID is invalid
    if not ObjectId.is_valid(id):
        abort(404)

    # A filter to locate the recipe in the database
    filter = {"_id": ObjectId(id), "creator": ObjectId(session["user"]["id"])}

    # Get the recipe with the given ID that also belongs to the logged in user
    recipe = mongo.db.recipes.find_one(filter)

    # Raise 404 error if a matching recipe is not found
    if recipe == None:
        abort(404)

    # If the form is posted
    if request.method == "POST":
        # Construct an update object with the form values
        update = {
            "name": request.form.get("name"),
            "time": request.form.get("time"),
            "serves": {
                "from": request.form.get("serves-from"),
                "to": request.form.get("serves-to")
            },
            "description": request.form.get("description"),
            "ingredients": [],
            "steps": []
        }

        # Update the recipe in the database
        mongo.db.recipes.update_one(filter, update)

        # Flash a successfully edited message
        flash("Changes saved")

        # Redirect to the my recipes page
        return redirect(url_for("recipes"))

    # Render the edit recipe template
    return render_template("recipes/edit.html", recipe=recipe)


edit.required_methods = ["GET", "POST"]


def delete(id):
    """View func to delete a recipe belonging to the logged in user."""

    # Redirect to login if the user is not logged in
    if session["user"] == None:
        return redirect(url_for("user/login"))

    # Raise 404 error if the ID is invalid
    if not ObjectId.is_valid(id):
        abort(404)

    # A filter to locate the recipe in the database
    filter = {"_id": ObjectId(id), "creator": ObjectId(session["user"]["id"])}

    # Get the recipe with the given ID that also belongs to the logged in user
    recipe = mongo.db.recipes.find_one(filter)

    # Raise 404 error if a matching recipe is not found
    if recipe == None:
        abort(404)

    # If the form is posted
    if request.method == "POST":
        # Delete the recipe with the given ID that also belongs to the logged in user
        mongo.db.recipes.delete_one(filter)

        # Flash a successfully deleted message
        flash("Recipe deleted")

        # Redirect to the my recipes page
        return redirect(url_for("recipes"))

    # Render the delete recipe template
    return render_template("recipes/delete.html", recipe=recipe)


delete.required_methods = ["GET", "POST"]
