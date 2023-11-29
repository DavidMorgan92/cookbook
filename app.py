import os
from flask import render_template
from flask_wtf.csrf import CSRFProtect
from setup import create_app
import user.user_views as user_views
import recipes_views

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
app.add_url_rule("/user/register", "user_register", view_func=user_views.register)
app.add_url_rule("/user/login", "user_login", view_func=user_views.login)
app.add_url_rule("/user/logout", "user_logout", view_func=user_views.logout)

# Register recipe views
app.add_url_rule("/recipes", "recipes_index", view_func=recipes_views.index)
app.add_url_rule("/recipes/edit/<id>", "recipes_edit", view_func=recipes_views.edit)
app.add_url_rule("/recipes/delete/<id>", "recipes_delete", view_func=recipes_views.delete)

if __name__ == "__main__":
    host = "0.0.0.0"
    port = int(os.environ.get("PORT"))
    debug = os.environ.get("ENVIRONMENT") == "Development"
    app.run(host=host, port=port, debug=debug)
