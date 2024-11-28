from flask import Flask


# This is a static file proxy for any subdomain registered to the app,
# it links to the main static folder. See the template files for more information.
def static_proxy(app: Flask):
    @app.route('/static/<path:filename>', subdomain='subdomain')
    def _static(filename):
        return app.send_static_file(filename)
