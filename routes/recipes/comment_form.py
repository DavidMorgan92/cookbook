from flask_wtf import FlaskForm
from wtforms import StringField, validators


class CommentForm(FlaskForm):
    text = StringField("Leave a comment", validators=[
        validators.DataRequired(),
        validators.Length(max=200)])
