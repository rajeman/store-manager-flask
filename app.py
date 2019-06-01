from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from config import config
import os
from flask_cors import CORS
from flask_restful import Api
from flask_bcrypt import Bcrypt
from api.resources.product import Product
from api.resources.user import User
from api.resources.auth import Auth
from api.resources.order import Order
from api.resources.profile import Profile

def create_app(config_name):
    flask_app = Flask(__name__)
    flask_app.config.from_object(config[config_name])
    CORS(flask_app)
    create_api(flask_app)
    return flask_app


def create_api(flask_app):
    api = Api(flask_app)
    api.add_resource(Product, '/api/v1/products', '/api/v1/products/<id>')
    api.add_resource(User, '/api/v1/auth/signup')
    api.add_resource(Auth, '/api/v1/auth/login')
    api.add_resource(Order, '/api/v1/sales', '/api/v1/sales/<id>')
    api.add_resource(Profile, '/api/v1/user')


app = create_app(os.getenv('APP_SETTINGS'))
db = SQLAlchemy(app)
jwt = JWTManager(app)
bcrypt = Bcrypt(app)
