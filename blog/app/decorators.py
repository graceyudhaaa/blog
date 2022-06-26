# @post.route("/create_post", methods=["GET", "POST"])
# @login_required
# def create_post():
#     if current_user.role != "admin":
#         abort(403)

from functools import wraps
from flask import abort
from flask_login import current_user


def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if current_user.role != "admin":
            abort(403)
        return f(*args, **kwargs)

    return decorated_function
