from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from api.helpers import (user_level, Attendant, Admin)


class Profile(Resource):

    @jwt_required
    @user_level(Admin, Attendant)
    def get(self, id=None):
        from api.models.user import User as UserModel
        from api.models.order import Order as OrderModel
        from app import bcrypt

        current_user = get_jwt_identity()
        existing_user = UserModel.find_by_email(current_user['email'].lower())
        order_entries_by_user = OrderModel.query.filter_by(user_id=existing_user.id).all()
        timestamp_to_order_entry = {}
        for order_entry in order_entries_by_user:
            timestamp_to_order_entry[order_entry.time_checked_out] = 'dummy'

        return {
            'message': "successfully fetched details",
            'userDetails': {
                'username': existing_user.name,
                'email': existing_user.email,
                'userId': existing_user.id,
                'level': existing_user.level,
                'totalOrders': len(timestamp_to_order_entry)
            }
        }
