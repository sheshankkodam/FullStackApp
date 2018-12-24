# python built-in packages
import urlparse
from backend_routes.AppName import AppName
from backend_routes.AppStatus import AppStatus
from flask import Flask
from flask_restful import Api
from flask_restful_swagger import swagger
from frontend_routes import FRONTEND


app = Flask(__name__)
app.register_blueprint(FRONTEND)

# Line 30 - 52 required for Swagger
API_BASE = "/api/"
API_VERSION = "v1/"


def with_prefix(api_version, relative_url):
    api_prefix = urlparse.urljoin(API_BASE, api_version)
    return urlparse.urljoin(api_prefix, relative_url)

api2 = swagger.docs(Api(app), apiVersion='1.0',
                    basePath='http://localhost:5000',
                    resourcePath='/',
                    produces=["application/json", "text/html"],
                    api_spec_url='/api/spec',
                    description='soup Backend API')

api2.add_resource(AppStatus, with_prefix(API_VERSION, 'status'))
api2.add_resource(AppName, with_prefix(API_VERSION, 'name'))


def run():
    app.run(debug=True)

if __name__ == '__main__':
    app.run(debug=True)
