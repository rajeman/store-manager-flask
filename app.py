from flask import Flask
from config import config
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

if __name__ == '__main__':
    create_app('development').run(port=5001)
