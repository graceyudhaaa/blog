from flask import Blueprint, render_template
from flask_login import login_required, current_user

from .forms import UpdateProfileForm

profile = Blueprint(
    "profile", __name__, template_folder="templates", static_folder="static"
)


@profile.route("/profile", methods=["GET", "POST"])
@login_required
def index():
    username = current_user.username
    title = f"Profile {username}"

    form = UpdateProfileForm()

    return render_template("profile.html", title=title, form=form)
