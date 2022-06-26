import datetime
from fileinput import filename
from flask import (
    Blueprint,
    redirect,
    render_template,
    current_app,
    abort,
    flash,
    url_for,
)
from flask_login import current_user, login_required
from bson.objectid import ObjectId

from ...decorators import admin_required

from .forms import PostForm
from ...utils import save_image

post = Blueprint("post", __name__, template_folder="templates", static_folder="static")


@post.route("/create_post", methods=["GET", "POST"])
@login_required
@admin_required
def create_post():

    title = "Create Post"
    form = PostForm()

    if form.validate_on_submit():
        post_title = form.title.data
        content = form.content.data
        category = form.category.data
        tags = [i.lower().strip() for i in form.tags.data.split(",")]
        author = {"_id": ObjectId(current_user._id), "username": current_user.username}
        created_at = datetime.datetime.utcnow()

        print(form.thumbnail.data)
        if form.thumbnail.data:
            thumbnail = save_image(form.thumbnail.data)
            thumbnail_url = url_for(
                "static", filename=f"user_upload/images/{thumbnail}"
            )
        else:
            thumbnail_url = url_for("static", filename="images/default_thumbnail.png")

        if form.thumbnail_alt.data:
            thumbnail_alt = form.thumbnail_alt.data
        else:
            thumbnail_alt = "Blog Thumbnail"

        post_dict = {
            "title": post_title,
            "thumbnail": thumbnail_url,
            "thumbnail_alt": thumbnail_alt,
            "content": content,
            "category": category,
            "tags": tags,
            "author": author,
            "created_at": created_at,
            "last_modified": created_at,
        }

        current_app.db["posts"].insert_one(post_dict)
        flash("your post has been created", "success")
        return redirect(url_for("home.index"))
    return render_template("create_post.html", title=title, form=form)
