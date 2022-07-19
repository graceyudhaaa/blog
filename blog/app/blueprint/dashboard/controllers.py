from flask import Blueprint, render_template, current_app
import pymongo

from ...utils import flatten_2d_list


dashboard = Blueprint(
    "dashboard", __name__, template_folder="templates", static_folder="static"
)


@dashboard.route("/dashboard")
def index():
    blog_post = list(
        current_app.db["posts"]
        .find({})
        .sort("last_modified", pymongo.DESCENDING)
    )

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
        .limit(5)
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
                    {"is_active": True},
                    {
                        "_id": 0,
                        "tags": 1,
                    },
                )
            ]
        )
    )

    print(tags)

    return render_template(
        "home.html",
        dashboard=True,
        blog_post=blog_post,
        recent_post=recent_post,
        categories=categories,
        tags=tags,
    )


# [
#     {
#         "_id": ObjectId("62b81df09c94012c8b88c6ec"),
#         "title": "Manajemen resiko",
#         "thumbnail": "/static/images/default_thumbnail.png",
#         "thumbnail_alt": "Blog Thumbnail",
#         "content": "Manajemen Resiko adalah mata kuliah yang sangat sulit",
#         "category": "Economy",
#         "tags": ["economy", "testing", "indonesian"],
#         "author": {
#             "_id": ObjectId("62b636073f865ba2d5bc01e0"),
#             "username": "graceyudha",
#         },
#         "created_at": datetime.datetime(2022, 6, 26, 8, 50, 56, 750000),
#         "last_modified": datetime.datetime(2022, 6, 26, 8, 50, 56, 750000),
#     },
#     {
#         "_id": ObjectId("62b82019d853b1c912ad6209"),
#         "title": "Quantum Physics",
#         "thumbnail": "/static/user_upload/images/ed3c8de976f98875.jpg",
#         "thumbnail_alt": "Quantum Physics",
#         "content": "Quantum Physics is hard",
#         "category": "Physics",
#         "tags": ["physics", "testing"],
#         "author": {
#             "_id": ObjectId("62b636073f865ba2d5bc01e0"),
#             "username": "graceyudha",
#         },
#         "created_at": datetime.datetime(2022, 6, 26, 9, 0, 9, 628000),
#         "last_modified": datetime.datetime(2022, 6, 26, 9, 0, 9, 628000),
#     },
# ]
