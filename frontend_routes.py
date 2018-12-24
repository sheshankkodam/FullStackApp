from flask import render_template, Blueprint


FRONTEND = Blueprint('frontend_routes', __name__, template_folder='templates', static_folder='frontend_static',
                     static_url_path='/frontend_static')
HEADERS = {'Cache-Control': 'private, max-age=0, no-cache',  # "max-age" overrides "expires"
           'Content-type': 'application/json'}


@FRONTEND.route('/home', methods=['GET'])
def home():
    return render_template("home.html")