import os
from flask import render_template
from flask_wtf.csrf import CSRFProtect
from setup import create_app
import user_views
import recipe_views

# Initialize environment variables
try:
    import env
    env.initialize()
except:
    pass

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
app.add_url_rule("/register", view_func=user_views.register,
                 methods=["GET", "POST"])
app.add_url_rule("/login", view_func=user_views.login, methods=["GET", "POST"])
app.add_url_rule("/logout", view_func=user_views.logout, methods=["POST"])

# Register recipe views
app.add_url_rule("/my_recipes", view_func=recipe_views.my_recipes)
app.add_url_rule("/edit_recipe/<id>",
                 view_func=recipe_views.edit_recipe, methods=["GET", "POST"])

if __name__ == "__main__":
    host = "0.0.0.0"
    port = int(os.environ.get("PORT"))
    debug = os.environ.get("ENVIRONMENT") == "Development"
    app.run(host=host, port=port, debug=debug)
