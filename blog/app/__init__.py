import os
from flask import Flask, render_template, url_for
from dotenv import load_dotenv
from pymongo import MongoClient

from .extensions import bcrypt, login_manager, ckeditor


from .config import *

from .blueprint.home.controllers import home
from .blueprint.about.controllers import about
from .blueprint.contact.controllers import contact
from .blueprint.auth.controllers import auth
from .blueprint.profile.controllers import profile
from .blueprint.post.controllers import post
from .blueprint.dashboard.controllers import dashboard

load_dotenv()

# ===================Error handling===================
def page_not_found(error):
    return render_template("404.html"), 404


def unauthorized(error):
    return render_template("403.html"), 403


# ===================Error handling===================


def create_app():
    app = Flask(__name__)
    client = MongoClient(os.environ["MONGODB_URI"])
    app.db = client["blog"]

    app.config["SECRET_KEY"] = SECRET_KEY

    if os.path.exists(f"{app.root_path}/static/user_upload/images") == False:
        os.makedirs(f"{app.root_path}/static/user_upload/images")

    # ===================Registering Extension===================
    bcrypt.init_app(app)

    login_manager.init_app(app)
    login_manager.login_view = "auth.login"
    login_manager.login_message_category = "info"

    ckeditor.init_app(app)
    app.config["CKEDITOR_PKG_TYPE"] = "standard-all"
    # ===================Registering Extension===================

    # ===================Registering Error===================
    app.register_error_handler(404, page_not_found)
    app.register_error_handler(403, unauthorized)
    # ===================Registering Error===================

    # ===================Registering Blueprint===================
    app.register_blueprint(home)
    app.register_blueprint(about)
    app.register_blueprint(contact)
    app.register_blueprint(auth)
    app.register_blueprint(profile)
    app.register_blueprint(post)
    app.register_blueprint(dashboard)
    # ===================Registering Blueprint===================

    return app
