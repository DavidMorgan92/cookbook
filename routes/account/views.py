from flask import render_template, session
from authorize import authorize


@authorize
def index():
    """View func to show the logged in user's account options."""
    
    # Get the ID of the logged in user
    id = session["user"]["id"]

    # Show the account index template with the logged in user's ID
    return render_template("account/index.html", id=id)
