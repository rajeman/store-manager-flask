from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config
import os
from flask_restful import Api
from api.resources.product import Product


def create_app(config_name):
    flask_app = Flask(__name__)
    flask_app.config.from_object(config[config_name])
    create_api(flask_app)
    return flask_app


def create_api(flask_app):
    api = Api(flask_app)
    api.add_resource(Product, '/api/v1/products', '/api/v1/products/<id>')


app = create_app(os.getenv('APP_SETTINGS'))
db = SQLAlchemy(app)
