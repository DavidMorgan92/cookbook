from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_uploads import UploadSet, IMAGES
from wtforms import StringField, FieldList, validators


image_upload_set = UploadSet("images", IMAGES)


class EditForm(FlaskForm):
    name = StringField("Name", validators=[validators.DataRequired()])

    description = StringField("Description", validators=[
                              validators.DataRequired()])

    time = StringField("Time", validators=[validators.DataRequired()])

    serves_from = StringField("Serves From", validators=[
                              validators.DataRequired()])

    serves_to = StringField("Serves To", validators=[
                            validators.DataRequired()])

    image = FileField("Image", validators=[FileAllowed(
        image_upload_set, "Only image file are allowed")])

    ingredients = FieldList(StringField(
        "Ingredient", [validators.DataRequired()]), min_entries=1, max_entries=100)

    steps = FieldList(StringField(
        "Step", [validators.DataRequired()]), min_entries=1, max_entries=100)
