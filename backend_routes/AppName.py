import httplib
from flask_restful import Resource


class AppName(Resource):
    def __init__(self):
        self.__HEADERS = {'Cache-Control': 'private, max-age=0, no-cache', 'Content-type': 'application/json'}

    def get(self):
        resp = {"name": "FullStack App"}
        return resp, httplib.OK, self.__HEADERS
