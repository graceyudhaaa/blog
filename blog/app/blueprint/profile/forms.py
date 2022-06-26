from flask_login import current_user
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask import current_app


class UpdateProfileForm(FlaskForm):
    username = StringField(
        "Username", validators=[DataRequired(), Length(min=1, max=50)]
    )
    email = StringField("Email", validators=[DataRequired(), Email()])
    submit = SubmitField("Save")

    def validate_username(self, username):
        if current_user.username != username.data:
            if (
                current_app.db["users"].count_documents({"username": username.data})
                != 0
            ):
                raise ValidationError(
                    f"username {username.data} already exists", "danger"
                )

    def validate_email(self, email):
        if current_user.email != email.data:
            if current_app.db["users"].count_documents({"email": email.data}) != 0:
                raise ValidationError(f"email {email.data} already exists", "danger")
