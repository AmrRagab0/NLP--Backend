from flask import Flask
from flask_restful import Api


def add_resources(app: Flask):
    api = Api(app)
    # api.add_resource(LoginResource, "/login")
