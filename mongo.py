from flask_pymongo import PyMongo
from bson.objectid import ObjectId

mongo = PyMongo()


def initialize(app):
    """Initialize the MongoDb connection."""

    mongo.init_app(app)


def get_user_by_name(name):
    """Return one user which matches the given name."""

    return mongo.db.users.find_one({"name": name})


def get_user_by_id(id):
    """Return one user which matches the given ID."""

    return mongo.db.users.find_one({"_id": ObjectId(id)})


def insert_user(user):
    """Insert a new user record."""

    return mongo.db.users.insert_one(user)


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
    ]))


def get_recipe_by_id(id):
    """Return one recipe which matches the given ID."""

    return mongo.db.recipes.find_one({"_id": ObjectId(id)})


def insert_recipe(recipe):
    """Insert a new recipe record."""

    return mongo.db.recipes.insert_one(recipe)


def update_recipe(id, update):
    """Update a recipe record."""

    return mongo.db.recipes.update_one(
        {"_id": ObjectId(id)},
        {"$set": update}
    )


def delete_recipe(id):
    """Delete a recipe record."""

    return mongo.db.recipes.delete_one({"_id": ObjectId(id)})
