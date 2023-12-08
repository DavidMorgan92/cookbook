from flask import redirect, url_for, request
from session import is_logged_in


def authorize(func):
    """Decorator to redirect a user to the login page if they are not authenticated."""

    def wrapper(**kwargs):
        # If user is not logged in return a redirect with a URL back to this route
        if not is_logged_in():
            return redirect(url_for("user_login", redirect_url=url_for(request.endpoint, **kwargs)))

        # If user is logged in then call the wrapped function
        return func(**kwargs)

    return wrapper
