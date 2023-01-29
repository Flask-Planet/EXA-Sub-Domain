from flask import render_template


def index_views(app):
    @app.route('/')
    def index():
        return render_template("www.html")

    @app.route('/', subdomain='subdomain')
    def sub():
        return render_template("subdomain.html")
