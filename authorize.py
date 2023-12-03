from flask import session, redirect, url_for, request


def authorize(func):
    """Decorator to redirect a user to the login page if they are not authenticated."""

    def wrapper(**kwargs):
        if not "user" in session:
            return redirect(url_for("user_login", redirect_url=url_for(request.endpoint, **kwargs)))

        return func(**kwargs)

    return wrapper
