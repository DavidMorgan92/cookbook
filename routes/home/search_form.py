from flask_wtf import FlaskForm
from wtforms import SearchField, validators


class SearchForm(FlaskForm):
    q = SearchField("Search all recipes", validators=[
                    validators.DataRequired(),
                    validators.Length(max=50)])
