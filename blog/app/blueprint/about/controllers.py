from flask import Blueprint, render_template

about = Blueprint(
    "about", __name__, template_folder="templates", static_folder="static"
)

# fake database here


@about.route("/about")
def index():
    title = "About"
    return render_template("about.html", title=title)