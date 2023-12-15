import os
from flask import render_template, Flask
from flask_wtf.csrf import CSRFProtect
import mongo
import routes.home.views as home_views
import routes.user.views as user_views
import routes.recipes.views as recipes_views
import routes.account.views as account_views
import routes.profile.views as profile_views
import field_list_extensions
import session

# Initialize environment variables
try:
    import env
    env.initialize()
except:
    pass

# Initialize extension methods for WTForms FieldList
field_list_extensions.initialize()

# Create and configure Flask app
app = Flask("Cook Book")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

# Add CSRF protection to app
csrf = CSRFProtect()
csrf.init_app(app)

# Initialize MongoDb connection
mongo.initialize(app)

# Provide session data getters to all view templates
app.context_processor(session.context_processor)

# Register home views
app.add_url_rule("/", "home_index", view_func=home_views.index)
app.add_url_rule("/search", "home_search", view_func=home_views.search)

# Register user views
app.add_url_rule("/user/register", "user_register",
                 view_func=user_views.register)
app.add_url_rule("/user/login", "user_login", view_func=user_views.login)
app.add_url_rule("/user/logout", "user_logout", view_func=user_views.logout)

# Register recipe views
app.add_url_rule("/recipes", "recipes_index", view_func=recipes_views.index)
app.add_url_rule("/recipes/<id>", "recipes_details",
                 view_func=recipes_views.details)
app.add_url_rule("/recipes/create", "recipes_create",
                 view_func=recipes_views.create)
app.add_url_rule("/recipes/edit/<id>", "recipes_edit",
                 view_func=recipes_views.edit)
app.add_url_rule("/recipes/edit_image/<id>",
                 "recipes_edit_image", view_func=recipes_views.edit_image)
app.add_url_rule("/recipes/delete/<id>", "recipes_delete",
                 view_func=recipes_views.delete)
app.add_url_rule("/recipes/favourite/<id>", "recipes_favourite",
                 view_func=recipes_views.favourite)
app.add_url_rule("/recipes/like/<id>", "recipes_like",
                 view_func=recipes_views.like)
app.add_url_rule("/recipes/favourites", "recipes_favourites",
                 view_func=recipes_views.favourites)
app.add_url_rule("/recipes/comment/<id>", "recipes_comment",
                 view_func=recipes_views.comment)

# Register account views
app.add_url_rule("/account", "account_index", view_func=account_views.index)
app.add_url_rule("/account/change_password", "account_change_password",
                 view_func=account_views.change_password)

# Register profile views
app.add_url_rule("/profile/<id>", "profile_index",
                 view_func=profile_views.index)

if __name__ == "__main__":
    host = "0.0.0.0"
    port = int(os.environ.get("PORT"))
    debug = os.environ.get("ENVIRONMENT") == "Development"
    app.run(host=host, port=port, debug=debug)
