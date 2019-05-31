from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from api.helpers import (
    valid_product,
    update_entity_fields,
    user_level,
    Attendant,
    Admin
)


class Product(Resource):

    @jwt_required
    @user_level(Admin)
    @valid_product(request)
    def post(self, id=None):
        from api.models.product import Product as ProductModel
        if id:
            return {'error': 'URL not found on this server'}, 404
        product = request.get_json()
        new_product = ProductModel(
            name=product['productName'],
            price=product['price'],
            minimum_inventory=product['minimumInventory'],
            quantity=product['productQuantity'])
        new_product.save_to_db()
        return {'message': '{} was successfully added'.format(product['productName'])}

    @jwt_required
    @user_level(Attendant, Admin)
    def get(self, id=None):
        from api.models.product import Product as ProductModel
        if id:
            product = ProductModel.find_by_id(id=id)
            if product:
                return {'message': 'successfully fetched product',
                        'product': product.json()}
            return {'error': 'Product not found'}, 404
        return {'message': 'successfully fetched products',
                'products': ProductModel.json_all(ProductModel.find_all())}

    @jwt_required
    @user_level(Admin)
    @valid_product(request)
    def put(self, id=None):
        if not id:
            return {'error': 'URL not found on this server'}, 404
        from api.models.product import Product as ProductModel
        product = request.get_json()
        current_product = ProductModel.find_by_id(id=id)
        if not current_product:
            return {'error': 'Product not found'}, 404
        update_entity_fields(current_product, name=product['productName'],
                             price=product['price'],
                             minimum_inventory=product['minimumInventory'],
                             quantity=product['productQuantity'])
        current_product.save_to_db()
        return {'message': 'successfully updated product'}

    @jwt_required
    @user_level(Admin)
    def delete(self, id=None):
        if not id:
            return {'error': 'URL not found on this server'}, 404
        from api.models.product import Product as ProductModel
        product = ProductModel.find_by_id(id=id)
        if not product:
            return {'error': 'Product not found'}, 404
        product.delete_from_db()
        return {'message': 'successfully deleted product'}
