from flask import render_template
from mongo import get_all_recipes_by_id_with_creator_name, get_user_by_id
from authorize import authorize
from session import logged_in_user_id


@authorize
def index():
    """View func to show a list of the logged in user's favourite recipes."""

    # Get the data for the logged in user
    user = get_user_by_id(logged_in_user_id())

    # Get the user's favourite recipes
    recipes = get_all_recipes_by_id_with_creator_name(user["favourites"])

    # Show all the recipes
    return render_template("favourites/index.html", recipes=recipes)
