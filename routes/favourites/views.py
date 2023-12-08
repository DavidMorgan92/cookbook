from flask import session, render_template
from bson.objectid import ObjectId
from setup import mongo
from authorize import authorize


@authorize
def index():
    """View func to show a list of the logged in user's favourite recipes."""

    # Get the data for the logged in user
    user = mongo.db.users.find_one({"_id": ObjectId(session["user"]["id"])})

    # Get the user's favourite recipes
    recipes = list(mongo.db.recipes.aggregate([
        {
            "$match": {
                "_id": { "$in": user["favourites"] }
            }
        },
        {
            "$lookup": {
                "from": "users",
                "localField": "creator_id",
                "foreignField": "_id",
                "as": "creator",
                "pipeline": [
                    {
                        "$project": {
                            "name": True
                        }
                    }
                ]
            }
        },
        {
            "$unwind": {
                "path": "$creator"
            }
        }
    ]))

    print(recipe["creator"] for recipe in recipes)

    # Show all the recipes
    return render_template("favourites/index.html", recipes=recipes)
