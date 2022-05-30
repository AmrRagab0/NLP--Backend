from flask import Flask
from flask_restful import Api

from app.auth.resources import LoginResource


def add_resources(app: Flask):
    api = Api(app)
    api.add_resource(LoginResource, "/login")
