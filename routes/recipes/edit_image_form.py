from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed


class EditImageForm(FlaskForm):
    image = FileField("Image", validators=[
        FileAllowed(["jpg", "png"], "Only JPG and PNG files are allowed")])
