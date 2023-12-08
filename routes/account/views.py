from flask import render_template
from authorize import authorize
from session import logged_in_user_id


@authorize
def index():
    """View func to show the logged in user's account options."""
    
    # Show the account index template with the logged in user's ID
    return render_template("account/index.html", id=logged_in_user_id())
