from flask import Flask
from flask_pymongo import PyMongo
import os

mongo = PyMongo()


def create_app():
    app = Flask("Cook Book")
    app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
    app.secret_key = os.environ.get("SECRET_KEY")

    mongo.init_app(app)

    return app
