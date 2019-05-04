from flask import request
from flask_restful import Resource
from api.helpers import valid_product


class Product(Resource):
    @valid_product(request)
    def post(self):
        from api.models.product import Product as ProductModel
        product = request.get_json()
        new_product = ProductModel(
            name=product['productName'],
            price=product['price'],
            minimum_inventory=product['minimumInventory'],
            quantity=product['productQuantity'])
        new_product.save_to_db()
        return {'message': '{} was successfully added'.format(product['productName'])}
