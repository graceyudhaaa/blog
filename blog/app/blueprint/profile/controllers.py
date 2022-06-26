import os
import secrets
from PIL import Image
from flask import (
    Blueprint,
    redirect,
    render_template,
    current_app,
    flash,
    request,
    url_for,
)
from flask_login import login_required, current_user
from bson.objectid import ObjectId

from .forms import UpdateProfileForm

profile = Blueprint(
    "profile", __name__, template_folder="templates", static_folder="static"
)


def save_image(form_picture):
    random_hex = secrets.token_hex(8)
    # blank one suppose to be filename
    _, file_extension = os.path.splitext(form_picture.filename)
    pic_filename = random_hex + file_extension
    pic_path = f"{current_app.root_path}/static/user_upload/images/{pic_filename}"

    output_size = (256, 256)
    image = Image.open(form_picture)
    image.thumbnail(output_size, Image.ANTIALIAS)
    image.save(pic_path, optimize=True, quality=20, dpi=[300, 300])

    return pic_filename


@profile.route("/profile", methods=["GET", "POST"])
@login_required
def index():
    title = f"Profile {current_user.username}"

    form = UpdateProfileForm()

    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data

        update = {"username": username, "email": email}

        if form.avatar.data:
            avatar = save_image(form.avatar.data)
            current_user.avatar = url_for(
                "static", filename=f"user_upload/images/{avatar}"
            )
            update["avatar"] = current_user.avatar

        current_user.username = username
        current_user.email = email

        current_app.db["users"].find_one_and_update(
            {"_id": ObjectId(current_user._id)}, {"$set": update}
        )

        flash("Your account has been updated", "success")
        return redirect(url_for("profile.index"))
    elif request.method == "GET":
        form.username.data = current_user.username
        form.email.data = current_user.email

    return render_template("profile.html", title=title, form=form)
