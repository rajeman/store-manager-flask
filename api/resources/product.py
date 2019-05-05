from flask import request
from flask_restful import Resource
from api.helpers import valid_product


class Product(Resource):
    @valid_product(request)
    def post(self, id=None):
        from api.models.product import Product as ProductModel
        product = request.get_json()
        new_product = ProductModel(
            name=product['productName'],
            price=product['price'],
            minimum_inventory=product['minimumInventory'],
            quantity=product['productQuantity'])
        new_product.save_to_db()
        return {'message': '{} was successfully added'.format(product['productName'])}

    def get(self, id=None):
        from api.models.product import Product as ProductModel
        if id:
            product = ProductModel.find_by_id(id=id)
            if product:
                return product.json()
            return {'error': 'Product not found'}, 404
        return ProductModel.json_all(ProductModel.find_all())
