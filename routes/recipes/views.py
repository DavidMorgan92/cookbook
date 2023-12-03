from flask import session, redirect, url_for, abort, render_template, request, flash
from bson.objectid import ObjectId
from base64 import b64encode
from setup import mongo
from authorize import authorize
from routes.recipes.edit_form import EditForm
from routes.recipes.edit_image_form import EditImageForm


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


def details(id):
    """View func to publicly show the details of a recipe."""

    # Raise 404 if the ID is invalid
    if not ObjectId.is_valid(id):
        abort(404)

    # Get the recipe with the given ID
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(id)})

    # Raise 404 if the recipe is not found
    if recipe == None:
        abort(404)

    # Render the details template with the recipe
    return render_template("recipes/details.html", recipe=recipe)


details.required_methods = ["GET"]


@authorize
def edit(id):
    """View func to edit a recipe belonging to the logged in user."""

    # Get a recipe belonging to the logged in user with the given ID
    filter = find_recipe_filter(id)
    recipe = find_recipe(filter)

    # Create the forms
    form = EditForm()
    image_form = EditImageForm()

    # If the form is posted and valid
    if form.validate_on_submit():
        # Construct an update object with the form values
        update = {
            "name": form.name.data,
            "description": form.description.data,
            "time_minutes": form.time.data,
            "serves": {
                "from": form.serves_from.data,
                "to": form.serves_to.data
            },
            "ingredients": form.ingredients.data,
            "steps": form.steps.data
        }

        # Update the recipe in the database
        mongo.db.recipes.update_one(filter, {"$set": update})

        # Flash a successfully edited message
        flash("Changes saved")

        # Redirect to the my recipes page
        return redirect(url_for("recipes_index"))

    if not form.is_submitted():
        # If form is not submitted populate the form with existing data
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
        # If form is submitted but invalid prepend an empty entry to each of the field lists to serve as a template
        form.ingredients.prepend_entry()
        form.steps.prepend_entry()

    # Render the edit recipe template
    return render_template("recipes/edit.html", form=form, image_form=image_form, recipe=recipe)


edit.required_methods = ["GET", "POST"]


@authorize
def edit_image(id):
    """View func to update the image of a recipe belonging to the logged in user."""

    # Create the edit image form
    image_form = EditImageForm()

    if image_form.validate():
        # Get the uploaded image as a base 64 encoded string
        image = request.files.get(image_form.image.name, None)
        image_data = b64encode(image.read()).decode() if image else None

        # Update the recipe in the database
        filter = find_recipe_filter(id)
        update = {"image_data": image_data}
        mongo.db.recipes.update_one(filter, {"$set": update})

        # Flash a successfully edited message
        flash("Changes saved")
    else:
        # Flash a validation error if the form is invalid
        flash("Only JPG and PNG files are accepted")

    return redirect(url_for("recipes_edit", id=id))


edit_image.required_methods = ["POST"]


@authorize
def delete(id):
    """View func to delete a recipe belonging to the logged in user."""

    # Get a recipe belonging to the logged in user and store the filter used to locate it
    recipe, filter = find_recipe(id)

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


def find_recipe_filter(id):
    """Create a filter to locate a recipe belonging to the logged in user by its ID."""

    # Raise 404 error if the ID is invalid
    if not ObjectId.is_valid(id):
        abort(404)

    # A filter to locate the recipe in the database
    return {"_id": ObjectId(id), "creator": ObjectId(session["user"]["id"])}


def find_recipe(filter):
    """
    Get a recipe belonging to the logged in user by its ID.
    """

    # Get a recipe that matches the filter
    recipe = mongo.db.recipes.find_one(filter)

    # Raise 404 error if a matching recipe is not found
    if recipe == None:
        abort(404)

    # Return recipe
    return recipe
