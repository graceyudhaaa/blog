import datetime
from fileinput import filename
from flask import (
    Blueprint,
    redirect,
    render_template,
    current_app,
    abort,
    flash,
    request,
    url_for,
)
from flask_login import current_user, login_required
from bson.objectid import ObjectId
from slugify import slugify
import pymongo

from ...decorators import admin_required

from .forms import PostForm
from ...utils import save_image, flatten_2d_list

post = Blueprint("post", __name__, template_folder="templates", static_folder="static")

# redirect /post route to home
@post.route("/post")
def redirect_to_home():
    return redirect(url_for("home.index"))


@post.route("/create_post", methods=["GET", "POST"])
@login_required
@admin_required
def create_post():

    title = "Create Post"
    form = PostForm()

    if form.validate_on_submit():
        post_title = form.title.data
        slug = slugify(form.slug.data)
        content = form.content.data
        category = form.category.data.lower()
        tags = [i.lower().strip() for i in form.tags.data.split(",")]
        author = {"_id": ObjectId(current_user._id), "username": current_user.username}
        created_at = datetime.datetime.utcnow()

        if form.thumbnail.data:
            thumbnail = save_image(form.thumbnail.data, (770, 770))
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
            "slug": slug,
            "content": content,
            "category": category,
            "tags": tags,
            "author": author,
            "created_at": created_at,
            "last_modified": created_at,
            "is_active": True,
        }

        current_app.db["posts"].insert_one(post_dict)
        flash("your post has been created", "success")
        return redirect(url_for("home.index"))
    return render_template(
        "form_post.html", title=title, form=form, legend="Create Post"
    )


@post.route("/post/<slug>")
def post_detail(slug):
    post_in_db = current_app.db["posts"].find_one(
        {
            "slug": slug,
        }
    )

    if not post_in_db:
        abort(404)

    if not post_in_db["is_active"]:
        if not current_user.is_authenticated or (current_user.role != "admin"):
            abort(404)

    title = post_in_db["title"].title()

    recent_post = list(
        current_app.db["posts"]
        .find(
            {"is_active": True},
            {
                "_id": 0,
                "title": 1,
                "slug": 1,
                "created_at": 1,
            },
        )
        .sort("created_at", pymongo.DESCENDING)
    )

    categories = set(
        [
            i["category"]
            for i in current_app.db["posts"].find(
                {"is_active": True},
                {
                    "_id": 0,
                    "category": 1,
                },
            )
        ]
    )

    tags = set(
        flatten_2d_list(
            [
                i["tags"]
                for i in current_app.db["posts"].find(
                    {},
                    {
                        "_id": 0,
                        "tags": 1,
                    },
                )
            ]
        )
    )

    return render_template(
        "post_detail.html",
        title=title,
        post=post_in_db,
        recent_post=recent_post,
        categories=categories,
        tags=tags,
    )


@post.route("/post/delete/<slug>")
def delete_post(slug):
    current_app.db["posts"].find_one_and_update(
        {"slug": slug}, {"$set": {"is_active": False}}
    )

    return redirect(request.referrer)


@post.route("/post/restore/<slug>")
def restore_post(slug):
    current_app.db["posts"].find_one_and_update(
        {"slug": slug}, {"$set": {"is_active": True}}
    )

    return redirect(request.referrer)


@post.route("/post/update/<slug>", methods=["GET", "POST"])
@login_required
@admin_required
def update_post(slug):
    post_in_db = current_app.db["posts"].find_one(
        {
            "slug": slug,
        }
    )

    if not post_in_db:
        abort(404)

    title = f"Update {post_in_db['title'].title()}"

    form = PostForm()

    if form.validate_on_submit():
        post_title = form.title.data
        new_slug = slugify(form.slug.data)
        content = form.content.data
        category = form.category.data.lower()
        tags = [i.lower().strip() for i in form.tags.data.split(",")]
        last_modified = datetime.datetime.utcnow()
        active = form.active.data

        post_dict = {
            "title": post_title,
            "slug": new_slug,
            "content": content,
            "category": category,
            "tags": tags,
            "last_modified": last_modified,
            "is_active": active,
        }

        if form.thumbnail_alt.data:
            thumbnail_alt = form.thumbnail_alt.data
            post_dict["thumbnail_alt"] = thumbnail_alt

        if form.thumbnail.data:
            thumbnail = save_image(form.thumbnail.data, (770, 770))
            thumbnail_url = url_for(
                "static", filename=f"user_upload/images/{thumbnail}"
            )
            post_dict["thumbnail"] = thumbnail_url

        current_app.db["posts"].find_one_and_update({"slug": slug}, {"$set": post_dict})

        flash("Your post has been updated", "success")
        return redirect(url_for("post.post_detail", slug=post_dict["slug"]))
    elif request.method == "GET":
        form.title.data = post_in_db["title"]
        form.slug.data = post_in_db["slug"]
        form.thumbnail_alt.data = post_in_db["thumbnail_alt"]
        form.content.data = post_in_db["content"]
        form.category.data = post_in_db["category"]
        form.tags.data = ", ".join(list(post_in_db["tags"]))
        form.active.data = post_in_db["is_active"]

    return render_template(
        "form_post.html", title=title, form=form, legend="Update Post"
    )
