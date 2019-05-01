from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config
import os
from flask_restful import Api
from api.student import Student


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    create_api(app)
    return app


def create_api(app):
    api = Api(app)
    api.add_resource(Student, '/student/<string:name>')

app = create_app(os.getenv('APP_SETTINGS'))
db = SQLAlchemy(app)
