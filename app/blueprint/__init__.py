from flask import Blueprint, current_app, render_template

blueprint = Blueprint(
    'blueprint',
    __name__,
    subdomain='blueprint',
    template_folder='templates',
)

@blueprint.route('/')
def index():
    return render_template('blueprint/blueprint.html')

# This is a static file proxy for the blueprint subdomain, it links to the main
# static folder. See the template files for more information.
@blueprint.route('/static/<path:filename>')
def _static(filename):
    return current_app.send_static_file(filename)
