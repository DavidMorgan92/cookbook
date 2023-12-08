import os
from flask import render_template
from flask_wtf.csrf import CSRFProtect
from setup import create_app
import routes.user.views as user_views
import routes.recipes.views as recipes_views
import routes.account.views as account_views
import routes.profile.views as profile_views
import routes.favourites.views as favourites_views
import field_list_extensions

# Initialize environment variables
try:
    import env
    env.initialize()
except:
    pass

# Initialize extension methods for WTForms FieldList
field_list_extensions.initialize()

# Create and configure Flask app and MongoDB connection
app = create_app()

# Add CSRF protection to app
csrf = CSRFProtect()
csrf.init_app(app)


# Register home view
@app.route("/")
def home():
    return render_template("home.html")


# Register user views
app.add_url_rule("/user/register", "user_register", view_func=user_views.register)
app.add_url_rule("/user/login", "user_login", view_func=user_views.login)
app.add_url_rule("/user/logout", "user_logout", view_func=user_views.logout)

# Register recipe views
app.add_url_rule("/recipes", "recipes_index", view_func=recipes_views.index)
app.add_url_rule("/recipes/<id>", "recipes_details", view_func=recipes_views.details)
app.add_url_rule("/recipes/create", "recipes_create", view_func=recipes_views.create)
app.add_url_rule("/recipes/edit/<id>", "recipes_edit", view_func=recipes_views.edit)
app.add_url_rule("/recipes/edit_image/<id>", "recipes_edit_image", view_func=recipes_views.edit_image)
app.add_url_rule("/recipes/delete/<id>", "recipes_delete", view_func=recipes_views.delete)

# Register account views
app.add_url_rule("/account", "account_index", view_func=account_views.index)

# Register profile views
app.add_url_rule("/profile/<id>", "profile_index", view_func=profile_views.index)

# Register favourites views
app.add_url_rule("/favourites", "favourites_index", view_func=favourites_views.index)

if __name__ == "__main__":
    host = "0.0.0.0"
    port = int(os.environ.get("PORT"))
    debug = os.environ.get("ENVIRONMENT") == "Development"
    app.run(host=host, port=port, debug=debug)
