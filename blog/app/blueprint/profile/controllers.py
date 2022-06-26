from flask import Blueprint, render_template
from flask_login import login_required, current_user

profile = Blueprint(
    "profile", __name__, template_folder="templates", static_folder="static"
)


@profile.route("/profile")
@login_required
def index():
    username = current_user.username
    title = f"Profile {username}"
    return render_template("profile.html", title=title)
