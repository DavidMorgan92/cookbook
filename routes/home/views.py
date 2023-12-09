from flask import render_template, request, redirect, url_for
from mongo import search_recipes
from routes.home.search_form import SearchForm


def index():
    """View func to show the home page."""

    form = SearchForm(meta={"csrf": False})

    # Show the home page
    return render_template("home/index.html", form=form)


index.required_methods = ["GET"]


def search():
    """View func to show search results."""

    form = SearchForm(request.args, meta={"csrf": False})

    if form.validate():
        recipes = search_recipes(form.q.data)
        
        return render_template("home/search.html", form=form, recipes=recipes)
    
    return redirect(url_for("home_index"))


search.required_methods = ["GET"]
