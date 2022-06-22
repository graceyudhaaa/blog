from flask import Flask
from .blueprint.home.views import home
from .blueprint.about.views import about
from .blueprint.contact.views import contact


def create_app():
    app = Flask(__name__)

    app.register_blueprint(home)
    app.register_blueprint(about)
    app.register_blueprint(contact)

    return app
