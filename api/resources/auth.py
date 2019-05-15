import os
from flask import request, jsonify
from flask_restful import Resource
from flask_jwt_extended import create_access_token


class Auth(Resource):
    def post(self):
        kwargs = request.get_json()
        if not kwargs:
            return {"msg": "Missing JSON in request"}, 400
        email = kwargs.get('email', '')
        password = kwargs.get('password', '')
        from api.models.user import User as UserModel
        from app import bcrypt
        existing_user = UserModel.find_by_email(email.lower())
        if existing_user and bcrypt.check_password_hash(
                existing_user.password, password):
            token = create_access_token(
                identity={'name': existing_user.name, 'id': existing_user.id,
                          'email': existing_user.email, 'level': existing_user.level})
            return {'message': 'Successfully logged in', 'token': token}
        return {'error': 'Invalid email or password'}, 401
