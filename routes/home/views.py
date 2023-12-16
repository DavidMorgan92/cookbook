from flask import render_template, request, redirect, url_for, flash
from mongo import search_recipes, get_popular_recipes
from routes.home.search_form import SearchForm
from routes.home.contact_form import ContactForm


def index():
    """View func to show the home page."""

    form = SearchForm(meta={"csrf": False})

    popular_recipes = get_popular_recipes(10)

    # Show the home page
    return render_template("home/index.html", form=form, popular_recipes=popular_recipes)


index.required_methods = ["GET"]


def search():
    """View func to show search results."""

    form = SearchForm(request.args, meta={"csrf": False})

    if form.validate():
        recipes = search_recipes(form.q.data)
        
        return render_template("home/search.html", form=form, recipes=recipes)
    
    return redirect(url_for("home_index"))


search.required_methods = ["GET"]


def contact():
    """View func to show contact form."""

    form = ContactForm()

    if form.validate_on_submit():
        flash("Message sent")

        return redirect(url_for("home_contact"))

    return render_template("home/contact.html", form=form)


contact.required_methods = ["GET", "POST"]
