from flask import Flask, render_template


def index_views(app: Flask):
    @app.route('/')
    def index():
        return render_template("www.html")

    @app.route('/', subdomain='subdomain')
    def sub():
        return render_template("subdomain.html")
