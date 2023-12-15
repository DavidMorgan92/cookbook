from flask import redirect, url_for, abort, render_template, request, flash
from bson.objectid import ObjectId
from base64 import b64encode
from mongo import get_recipes_by_creator_id, get_recipe_by_id, get_recipe_by_id_with_comment_creator_names, insert_recipe, update_recipe, delete_recipe, get_user_by_id, favourite_recipe, unfavourite_recipe, get_all_recipes_by_id_with_creator_name, insert_comment, like_recipe, unlike_recipe
from authorize import authorize
from routes.recipes.edit_form import EditForm
from routes.recipes.edit_image_form import EditImageForm
from routes.recipes.comment_form import CommentForm
from session import is_logged_in, logged_in_user_id


@authorize
def index():
    """View func to show a list of recipes belonging to the logged in user."""

    # Get list of recipes belonging to the logged in user
    recipes = get_recipes_by_creator_id(logged_in_user_id())

    # Render template with list of recipes
    return render_template("recipes/index.html", recipes=recipes)


index.required_methods = ["GET"]


def details(id):
    """View func to publicly show the details of a recipe."""

    # Raise 404 if the ID is invalid
    if not ObjectId.is_valid(id):
        abort(404)

    # Get the recipe with the given ID
    recipe = get_recipe_by_id_with_comment_creator_names(id)

    # Raise 404 if the recipe is not found
    if recipe == None:
        abort(404)

    # Default is_favourite to False so when an anonymous user tries to select it they will be taken to the login page
    is_favourite = False

    # Default is_liked to False
    is_liked = False

    # Get whether the recipe is a favourite of the user's
    if is_logged_in():
        user_id = logged_in_user_id()
        user = get_user_by_id(user_id)
        is_favourite = ObjectId(id) in user["favourites"]
        is_liked = ObjectId(user_id) in recipe["liked_by_ids"]

    comment_form = CommentForm()

    # Render the details template with the recipe
    return render_template("recipes/details.html", recipe=recipe, is_favourite=is_favourite, is_liked=is_liked, comment_form=comment_form)


details.required_methods = ["GET"]


@authorize
def create():
    # Create a default recipe
    recipe = {
        "name": "New recipe",
        "description": "",
        "time_minutes": 0,
        "serves": {
            "from": 1,
            "to": 1
        },
        "image_data": None,
        "ingredients": [],
        "steps": [],
        "creator_id": ObjectId(logged_in_user_id())
    }

    # Insert the new recipe into the database
    insert_result = insert_recipe(recipe)

    # Redirect to the edit view for the new recipe
    return redirect(url_for("recipes_edit", id=insert_result.inserted_id))


create.required_methods = ["POST"]


@authorize
def edit(id):
    """View func to edit a recipe belonging to the logged in user."""

    # Get recipe, raise 404 if it doesn't exist
    recipe = get_recipe(id)

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
        update_recipe(id, update)

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
        # Flash changes not saved message
        flash("Changes not saved")

        # If form is submitted but invalid prepend an empty entry to each of the field lists to serve as a template
        form.ingredients.prepend_entry()
        form.steps.prepend_entry()

    # Render the edit recipe template
    return render_template("recipes/edit.html", form=form, image_form=image_form, recipe=recipe)


edit.required_methods = ["GET", "POST"]


@authorize
def edit_image(id):
    """View func to update the image of a recipe belonging to the logged in user."""

    # Raise 404 if the ID is invalid
    if not ObjectId.is_valid(id):
        abort(404)

    # Create the edit image form
    image_form = EditImageForm()

    if image_form.validate():
        # Get the uploaded image as a base 64 encoded string
        image = request.files.get(image_form.image.name, None)
        image_data = b64encode(image.read()).decode() if image else None

        # Update the recipe in the database
        update = {"image_data": image_data}
        update_recipe(id, update)

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

    # Get recipe, abort 404 if it doesn't exist
    recipe = get_recipe(id)

    # If the form is posted
    if request.method == "POST":
        # Delete the recipe with the given ID that also belongs to the logged in user
        delete_recipe(id)

        # Flash a successfully deleted message
        flash("Recipe deleted")

        # Redirect to the my recipes page
        return redirect(url_for("recipes_index"))

    # Render the delete recipe template
    return render_template("recipes/delete.html", recipe=recipe)


delete.required_methods = ["GET", "POST"]


@authorize
def favourite(id):
    """Add a recipe to the logged in user's favourites."""

    # Check recipe exists, abort 404 if not
    get_recipe(id)

    # Get the set query parameter
    set_flag = request.args.get("set", None)

    match set_flag:
        case "on":
            # Add the recipe to the logged in user's favourites
            favourite_recipe(logged_in_user_id(), id)

            # Flash a success message
            flash("Added to favourites")

        case "off":
            # Remove the recipe from the logged in user's favourites
            unfavourite_recipe(logged_in_user_id(), id)

            # Flash a success message
            flash("Removed from favourites")

    # Redirect to the recipe details page
    return redirect(url_for("recipes_details", id=id))


favourite.required_methods = ["POST"]


@authorize
def like(id):
    """Add the logged in user to the recipe's likes array."""

    # Check recipe exists, abort 404 if not
    get_recipe(id)

    # Get the set query parameter
    set_flag = request.args.get("set", None)

    match set_flag:
        case "on":
            # Add the user ID to the recipe's likes array
            like_recipe(logged_in_user_id(), id)

            # Flash a success message
            flash("Added to likes")

        case "off":
            # Remove the user ID from the recipe's likes array
            unlike_recipe(logged_in_user_id(), id)

            # Flash a success message
            flash("Removed from likes")

    # Redirect to the recipe details page
    return redirect(url_for("recipes_details", id=id))


like.required_methods = ["POST"]


@authorize
def favourites():
    """View func to show a list of the logged in user's favourite recipes."""

    # Get the data for the logged in user
    user = get_user_by_id(logged_in_user_id())

    # Get the user's favourite recipes
    recipes = get_all_recipes_by_id_with_creator_name(user["favourites"])

    # Show all the recipes
    return render_template("recipes/favourites.html", recipes=recipes)


favourites.required_methods = ["GET"]


@authorize
def comment(id):
    """View func to submit a comment to a recipe."""

    comment_form = CommentForm()

    if comment_form.validate():
        insert_comment(id, logged_in_user_id(), comment_form.text.data)

        flash("Comment saved")

    return redirect(url_for("recipes_details", id=id))


comment.required_methods = ["POST"]


def get_recipe(id):
    """Get a recipe by its ID or raise a 404 error if it doesn't."""

    # Raise 404 if the ID is invalid
    if not ObjectId.is_valid(id):
        abort(404)

    # Get a recipe belonging to the logged in user with the given ID
    recipe = get_recipe_by_id(id)

    # Raise 404 if the recipe is not found
    if recipe == None:
        abort(404)

    return recipe
