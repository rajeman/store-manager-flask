import os
from flask import request
from flask_restful import Resource
from api.helpers import valid_user_details


class User(Resource):
    @valid_user_details(request)
    def post(self, id=None):
        from api.models.user import User as UserModel
        user = request.get_json()
        existing_user = UserModel.find_by_email(user['email'].lower())
        if existing_user:
            return {'error': 'email in use'}, 409
        new_user = UserModel(
            name=user['name'],
            email=user['email'].lower(),
            password=os.getenv('DEFAULT_USER_PASSWORD'),
            level=1
        )
        new_user.save_to_db()
        return {'message': 'account created for {}'.format(user['name'])}
