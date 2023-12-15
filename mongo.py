from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timezone

mongo = PyMongo()


def initialize(app):
    """Initialize the MongoDb connection."""

    mongo.init_app(app)


def get_user_by_name(name):
    """Return one user which matches the given name."""

    return mongo.db.users.find_one({"name": name})


def get_user_by_name_and_password(name, password):
    """Return a user with the given name and password, otherwise return None."""

    # Find a user with the given name
    user = get_user_by_name(name)

    # Return None if the username does not match or the password is incorrect
    if user == None or not check_password_hash(user["password_hash"], password):
        return None

    # Otherwise return the user object
    return user


def get_user_by_id_and_password(id, password):
    # Find a user with the given ID
    user = get_user_by_id(id)

    # Return None if the username does not match or the password is incorrect
    if user == None or not check_password_hash(user["password_hash"], password):
        return None

    # Otherwise return the user object
    return user


def user_exists(name):
    """Returns True if a user with the given name exists."""

    return get_user_by_name(name) != None


def get_user_by_id(id):
    """Return one user which matches the given ID."""

    return mongo.db.users.find_one({"_id": ObjectId(id)})


def insert_user(username, password):
    """Insert a new user record."""

    user = {
        "name": username,
        "password_hash": generate_password_hash(password)
    }

    return mongo.db.users.insert_one(user)


def update_user_password(id, oldPassword, newPassword):
    """Update a user's password."""

    user = get_user_by_id_and_password(id, oldPassword)

    if user == None:
        return None

    return mongo.db.users.update_one({"_id": ObjectId(id)}, {"$set": {"password_hash": generate_password_hash(newPassword)}})


def get_recipes_by_creator_id(creator_id):
    """Get all recipes created by the user with the given ID."""

    return list(mongo.db.recipes.find({"creator_id": ObjectId(creator_id)}))


def get_all_recipes_by_id_with_creator_name(recipe_ids):
    """Get all recipes with the given IDs and their creator's user name."""

    return list(mongo.db.recipes.aggregate([
        {
            # Match IDs in recipe_ids
            "$match": {
                "_id": {"$in": recipe_ids}
            }
        },
        # Add recipe creator's name to returned objects
        *add_creator_name()
    ]))


def get_recipe_by_id(id):
    """Return one recipe which matches the given ID."""

    return mongo.db.recipes.find_one({"_id": ObjectId(id)})


def get_recipe_by_id_with_comment_creator_names(id):
    """Return one recipe which matches the given ID with its comments array containing their creators' names."""

    # https://copyprogramming.com/howto/mongodb-lookup-on-array-of-objects-with-reference-objectid
    recipes = mongo.db.recipes.aggregate([
        {
            "$match": {
                "_id": ObjectId(id)
            }
        },
        {
            "$lookup": {
                "from": "users",
                "localField": "comments.creator_id",
                "foreignField": "_id",
                "as": "comment_creators",
                "pipeline": [
                    {
                        # Only get the users' names
                        "$project": {"name": True}
                    }
                ]
            }
        },
        {
            "$set": {
                "comments": {
                    "$sortArray": {
                        "input": {
                            "$map": {
                                "input": "$comments",
                                "in": {
                                    "$mergeObjects": [
                                        "$$this",
                                        {
                                            "creator": {
                                                "$arrayElemAt": [
                                                    "$comment_creators",
                                                    {
                                                        "$indexOfArray": ["$comment_creators._id", "$$this.creator_id"]
                                                    }
                                                ]
                                            }
                                        }
                                    ]
                                }
                            }
                        },
                        "sortBy": {"created_at": -1}
                    }
                }
            }
        },
        {
            "$unset": "comment_creators"
        }
    ])

    return recipes.try_next()


def insert_recipe(recipe):
    """Insert a new recipe record."""

    return mongo.db.recipes.insert_one(recipe)


def insert_comment(recipe_id, creator_id, text):
    """Insert a new comment to a recipe."""

    return mongo.db.recipes.update_one({"_id": ObjectId(recipe_id)}, {
        "$push": {
            "comments": {
                "created_at": datetime.now(timezone.utc),
                "creator_id": ObjectId(creator_id),
                "text": text
            }
        }
    })


def update_recipe(id, update):
    """Update a recipe record."""

    return mongo.db.recipes.update_one({"_id": ObjectId(id)}, {"$set": update})


def delete_recipe(id):
    """Delete a recipe record."""

    return mongo.db.recipes.delete_one({"_id": ObjectId(id)})


def like_recipe(user_id, recipe_id):
    """Add a user's ID to a recipe's likes array."""

    return mongo.db.recipes.update_one({"_id": ObjectId(recipe_id)}, {"$addToSet": {"liked_by_ids": ObjectId(user_id)}})


def unlike_recipe(user_id, recipe_id):
    """Remove a user's ID from a recipe's likes array."""

    return mongo.db.recipes.update_one({"_id": ObjectId(recipe_id)}, {"$pull": {"liked_by_ids": ObjectId(user_id)}})


def favourite_recipe(user_id, recipe_id):
    """Add a recipe to the user's favourites array."""

    return mongo.db.users.update_one({"_id": ObjectId(user_id)}, {
        "$addToSet": {"favourites": ObjectId(recipe_id)}})


def unfavourite_recipe(user_id, recipe_id):
    """Remove a recipe from the user's favourites array."""

    return mongo.db.users.update_one({"_id": ObjectId(user_id)}, {
        "$pull": {"favourites": ObjectId(recipe_id)}})


def search_recipes(query):
    """Return a list of recipes that match the search query."""

    return list(mongo.db.recipes.aggregate([
        {
            "$search": {
                "index": "default",
                "text": {
                    "path": "name",
                    "query": query,
                    "fuzzy": {}
                }
            }
        },
        # Add recipe creator's name to returned objects
        *add_creator_name()
    ]))


def get_popular_recipes(limit):
    """Return a list of the most popular recipes."""

    return list(mongo.db.recipes.aggregate([
        {
            "$addFields": {"number_of_likes": {"$size": "$liked_by_ids"}}
        },
        {
            "$sort": {"number_of_likes": -1}
        },
        {
            "$limit": limit
        },
        *add_creator_name()
    ]))


def get_categories():
    """Return all categories."""

    return list(mongo.db.categories.find())


def add_creator_name():
    """Return elements of an aggregate pipeline that will add the recipe creator's name to the returned objects."""

    return [
        {
            # Look up related user objects
            "$lookup": {
                "from": "users",
                "localField": "creator_id",
                "foreignField": "_id",
                "as": "creator",
                "pipeline": [
                    {
                        # Only get the users' names
                        "$project": {"name": True}
                    }
                ]
            }
        },
        {
            # Unwind the related user lookup from an array to an object
            "$unwind": {"path": "$creator"}
        }
    ]
