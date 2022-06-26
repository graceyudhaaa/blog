import re
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


@profile.route("/profile", methods=["GET", "POST"])
@login_required
def index():
    title = f"Profile {current_user.username}"

    form = UpdateProfileForm()

    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data

        update = {"username": username, "email": email}

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
