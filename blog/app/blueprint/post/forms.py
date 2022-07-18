from ast import Sub
from turtle import title
from flask_wtf import FlaskForm
from slugify import slugify
from wtforms import StringField, SubmitField, BooleanField, TextAreaField
from flask_ckeditor import CKEditorField
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import DataRequired, ValidationError, Length
from flask import current_app, request


class PostForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    slug = StringField("Slug", validators=[DataRequired()])
    thumbnail = FileField("Thumbnail", validators=[FileAllowed(["jpg", "png"])])
    thumbnail_alt = StringField("Thumbnail Alt-Text", validators=[])
    description = TextAreaField(
        "Description", validators=[DataRequired(), Length(max=500)]
    )
    content = CKEditorField("Content", validators=[DataRequired()])
    category = StringField("Category", validators=[DataRequired()])
    tags = StringField("Tags", validators=[DataRequired()])
    active = BooleanField("Active")
    submit = SubmitField("Post")

    def validate_slug(self, slug):
        if request.path.split("/")[-1] != slug.data:
            if (
                current_app.db["posts"].count_documents({"slug": slugify(slug.data)})
                != 0
            ):
                raise ValidationError(f"slug {slug.data} already exists", "danger")
