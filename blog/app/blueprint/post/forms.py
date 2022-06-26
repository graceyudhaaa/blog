from ast import Sub
from turtle import title
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask import current_app


class PostForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    thumbnail = FileField("Thumbnail", validators=[FileAllowed(["jpg", "png"])])
    thumbnail_alt = StringField("Thumbnail Alt-Text", validators=[])
    content = TextAreaField("Content", validators=[DataRequired()])
    category = StringField("Category", validators=[DataRequired()])
    tags = StringField("Tags", validators=[DataRequired()])
    submit = SubmitField("Post")
