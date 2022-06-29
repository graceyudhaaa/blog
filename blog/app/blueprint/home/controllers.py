from flask import Blueprint, render_template, current_app
import pymongo

from ...utils import flatten_2d_list
from .models import Home


home = Blueprint("home", __name__, template_folder="templates", static_folder="static")
db = Home(current_app)


@home.route("/")
def index():
    blog_post = db.get_post_limit(5, {"is_active": True})

    recent_post = db.get_post(
        {"is_active": True}, {"_id": 0, "title": 1, "slug": 1, "created_at": 1}
    )

    categories = set(
        [
            i["category"]
            for i in db.get_post({"is_active": True}, {"_id": 0, "category": 1})
        ]
    )

    tags = set(
        flatten_2d_list(
            [i["tags"] for i in db.get_post({"is_active": True}, {"_id": 0, "tags": 1})]
        )
    )

    return render_template(
        "home.html",
        blog_post=blog_post,
        recent_post=recent_post,
        categories=categories,
        tags=tags,
    )
