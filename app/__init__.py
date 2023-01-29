from flask import Flask

# this import needs to be relative (.views.ind...) as views is not a package
from .views.index import index_views


def create_app():
    app = Flask(__name__)
    app.config["SERVER_NAME"] = "site.local:5000"

    index_views(app)

    return app
