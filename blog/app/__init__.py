import os
import datetime
from flask import Flask
from dotenv import load_dotenv
from pymongo import MongoClient

from .extensions import bcrypt, login_manager


from .config import *

from .blueprint.home.controllers import home
from .blueprint.about.controllers import about
from .blueprint.contact.controllers import contact
from .blueprint.auth.controllers import auth

load_dotenv()


def create_app():
    app = Flask(__name__)
    client = MongoClient(os.environ["MONGODB_URI"])
    app.db = client["blog"]

    app.config["SECRET_KEY"] = SECRET_KEY

    bcrypt.init_app(app)
    login_manager.init_app(app)

    app.register_blueprint(home)
    app.register_blueprint(about)
    app.register_blueprint(contact)
    app.register_blueprint(auth)

    return app
