import os
from flask import Flask, render_template
from flask_pymongo import PyMongo

# Initialize environment variables
try:
    import env
    env.initialize()
except:
    pass

# Create and configure Flask app and MongoDB connection
app = Flask("Cook Book")
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")
mongo = PyMongo(app)


@app.route("/")
def home():
    return render_template("home.html")


if __name__ == "__main__":
    host = "0.0.0.0"
    port = int(os.environ.get("PORT"))
    debug = os.environ.get("ENVIRONMENT") == "Development"
    app.run(host=host, port=port, debug=debug)
