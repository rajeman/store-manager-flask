import os
import time
from flask import request
from flask_restful import Resource, abort
from api.helpers import valid_user_details
from flask_jwt_extended import jwt_required, get_jwt_identity
from api.helpers import (valid_order_items, user_level, Attendant, Admin)


class Order(Resource):

    @jwt_required
    @user_level(Attendant)
    @valid_order_items(request)
    def post(self, id=None):
        order_items = request.get_json().get('products')
        current_user = get_jwt_identity()
        from api.models.order import Order as OrderModel
        from api.models.product import Product as ProductModel
        time_checked_out = int(round(time.time() * 1000))
        order_price = 0
        order_quantity = 0
        for order_item in order_items:
            actual_product = ProductModel.find_by_id(order_item['productId'])
            actual_product.quantity -= order_item['productQuantity']
            new_order = OrderModel(
                user_id=current_user['id'],
                time_checked_out=time_checked_out,
                product_price=actual_product.price,
                product_quantity=order_item['productQuantity'],
                product_id=order_item['productId']
            )
            actual_product.save_without_commit()
            new_order.save_without_commit()
            order_price += actual_product.price
            order_quantity += order_item['productQuantity']
        from app import db
        db.session.commit()
        return {'message': 'Successfully created order',
                'orderDetails': {
                    "user_id": current_user['id'],
                    "time_checked_out": str(time_checked_out),
                    "order_price": order_price,
                    "order_quantity": order_quantity
                }
            }

    @jwt_required
    @user_level(Admin, Attendant)
    def get(self, id=None):
        from api.models.order import Order as OrderModel
        from api.models.user import User as UserModel
        from api.models.product import Product as ProductModel

        current_user = get_jwt_identity()
        if id:
            if not (id.isdigit() and int(id) < (2 ** 63) - 1):
                abort(400, error='invalid order timestamp')
            order_items = OrderModel.query.filter_by(time_checked_out=id).join(UserModel).join(ProductModel).all()
            if not order_items:
                abort(404, error='order not found')
            if current_user['level'] == Attendant and not (current_user['id'] == order_items[0].user_id):
                abort(401, error='You are not authorized to view this order')
            order_item_result = []
            for order_item in order_items:
                order_item_result.append({
                    'user_id': order_item.user.id,
                    'time_checked_out': order_item.time_checked_out,
                    'product_name': order_item.product.name,
                    'product_price': order_item.product_price,
                    'product_quantity': order_item.product_quantity,
                    'product_id': order_item.product.id,
                    'total_price': order_item.product_price * order_item.product_quantity,
                    'user_name': order_item.user.name,
                    'user_id': order_item.user.id
                })

            return {'message': 'successfully fetched order',
                    'orderDetails': order_item_result
            }

        all_orders = []
        if current_user['level'] == Attendant:
            all_orders = OrderModel.query.join(UserModel).filter(
                UserModel.id==current_user['id']).all()
        else:
            all_orders = OrderModel.query.join(UserModel).all()
        timestamp_to_order = {}
        for order in all_orders:
            order_timestamp = order.time_checked_out

            if timestamp_to_order.get(order_timestamp):
                current_order = timestamp_to_order[order_timestamp]
                current_order['order_quantity'] += order.product_quantity
                current_order['order_price'] += order.product_price * order.product_quantity
            else:
                timestamp_to_order[order_timestamp] = {
                    'order_id': order.id,
                    'user_id': order.user_id,
                    'user_name': order.user.name,
                    'time_checked_out': order.time_checked_out,
                    'order_price': order.product_price * order.product_quantity,
                    'order_quantity': order.product_quantity
                }

        return { 'message': 'successfully fetched orders',
                 'orders': list(timestamp_to_order.values())
                }
