from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_uploads import UploadSet, IMAGES
from wtforms import StringField, FieldList, IntegerRangeField, IntegerField, TextAreaField, validators, ValidationError


image_upload_set = UploadSet("images", IMAGES)


class EditForm(FlaskForm):
    name = StringField("Name", validators=[
        validators.DataRequired(),
        validators.length(max=50)])

    description = TextAreaField("Description", validators=[
        validators.DataRequired(),
        validators.Length(max=500)])

    time = IntegerField("Time (minutes)", validators=[
        validators.DataRequired(),
        validators.NumberRange(min=1, max=600)])

    serves_from = IntegerRangeField("Serves from", validators=[
        validators.DataRequired(),
        validators.NumberRange(min=1, max=10)])

    serves_to = IntegerRangeField("Serves to", validators=[
        validators.DataRequired(),
        validators.NumberRange(min=1, max=10)])

    image = FileField("Image", validators=[
        FileAllowed(image_upload_set, "Only image file are allowed")])

    ingredients = FieldList(StringField(
        "Ingredient", [validators.DataRequired()]), min_entries=1)

    steps = FieldList(StringField(
        "Step", [validators.DataRequired()]), min_entries=1)

    def validate_serves_from(form, field):
        """Raise a validation error if the serves_from field is greater than the serves_to field."""

        if field.data > form.serves_to.data:
            raise ValidationError(
                'Serves from must be less than or equal to serves to')

    def validate_serves_to(form, field):
        """Raise a validation error if the serves_to field is less than the serves_from field."""

        if field.data < form.serves_from.data:
            raise ValidationError(
                'Serves to must be greater than or equal to serves from')