import httplib
from time import time
from flask_restful import Resource
from flask_restful_swagger import swagger
from os.path import join, dirname, abspath, isfile

SERVER_START_TIME = int(round(time() * 1000))

version_file = join(abspath(join(dirname(dirname(dirname(__file__))))), "VERSION")


class AppStatus(Resource):
    def __init__(self):
        self.__HEADERS = {'Cache-Control': 'private, max-age=0, no-cache', 'Content-type': 'application/json'}

    @swagger.operation(
        notes="Get status",
        nickname="get_status",
        responseMessages=[
            {
                "code": 404,
                "message": "App is Down"
            }
        ]
    )
    def get(self):
        version = file.read(open(version_file, 'r')) if isfile(version_file) else "Missing version file"
        uptime = int(round(time() * 1000)) - SERVER_START_TIME
        successful_json = {"app": "frontend sample", "status": "Up and Listening", "uptime": uptime, "version": version}
        return successful_json, httplib.OK, self.__HEADERS
