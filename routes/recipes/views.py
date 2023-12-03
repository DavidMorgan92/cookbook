from flask import session, redirect, url_for, abort, render_template, request, flash
from bson.objectid import ObjectId
from base64 import b64encode
from setup import mongo
from routes.recipes.edit_form import EditForm
from authorize import authorize


@authorize
def index():
    """View func to show a list of recipes belonging to the logged in user."""

    # A filter to locate the logged in user's recipes in the database
    filter = {"creator": ObjectId(session["user"]["id"])}

    # Get list of recipes belonging to the logged in user
    recipes = list(mongo.db.recipes.find(filter))

    # Render template with list of recipes
    return render_template("recipes/index.html", recipes=recipes)


index.required_methods = ["GET"]


@authorize
def edit(id):
    """View func to edit a recipe belonging to the logged in user."""

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

    # Create the form
    form = EditForm()

    # If the form is posted and valid
    if form.validate_on_submit():
        image = request.files.get(form.image.name, None)
        image_data = b64encode(image.read()).decode() if image else None

        # Construct an update object with the form values
        update = {
            "name": form.name.data,
            "description": form.description.data,
            "time_minutes": form.time.data,
            "serves": {
                "from": form.serves_from.data,
                "to": form.serves_to.data
            },
            "image_data": image_data,
            "ingredients": form.ingredients.data,
            "steps": form.steps.data
        }

        # Update the recipe in the database
        mongo.db.recipes.update_one(filter, {"$set": update})

        # Flash a successfully edited message
        flash("Changes saved")

        # Redirect to the my recipes page
        return redirect(url_for("recipes_index"))

    # Populate the form with existing data
    if not form.is_submitted():
        form.name.data = recipe["name"]
        form.description.data = recipe["description"]
        form.time.data = recipe["time_minutes"]
        form.serves_from.data = recipe["serves"]["from"]
        form.serves_to.data = recipe["serves"]["to"]

        for ingredient in recipe["ingredients"]:
            form.ingredients.append_entry(ingredient)

        for step in recipe["steps"]:
            form.steps.append_entry(step)
    else:
        form.ingredients.prepend_entry()
        form.steps.prepend_entry()

    # Render the edit recipe template
    return render_template("recipes/edit.html", form=form, recipe=recipe)


edit.required_methods = ["GET", "POST"]


@authorize
def delete(id):
    """View func to delete a recipe belonging to the logged in user."""

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
        return redirect(url_for("recipes_index"))

    # Render the delete recipe template
    return render_template("recipes/delete.html", recipe=recipe)


delete.required_methods = ["GET", "POST"]
