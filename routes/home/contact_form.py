from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, TextAreaField, validators


class ContactForm(FlaskForm):
    name = StringField("Name", validators=[
                       validators.DataRequired(), validators.Length(max=50)])

    email = EmailField("Email", validators=[validators.DataRequired()])

    message = TextAreaField("Message", validators=[
                            validators.DataRequired(), validators.Length(max=1000)])
