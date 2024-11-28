from flask import Flask

# this import needs to be relative (.views.ind...) as views is not a package
from .blueprint import blueprint
from .views.index import index_views
from .views.static_proxy import static_proxy



def create_app():
    app = Flask(__name__)
    app.subdomain_matching = True
    app.config["SERVER_NAME"] = "site.local:5000"

    index_views(app)
    static_proxy(app)

    app.register_blueprint(blueprint)

    return app
