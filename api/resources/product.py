from flask import request
from flask_restful import Resource
from api.helpers import valid_product, update_entity_fields


class Product(Resource):
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

    def get(self, id=None):
        from api.models.product import Product as ProductModel
        if id:
            product = ProductModel.find_by_id(id=id)
            if product:
                return product.json()
            return {'error': 'Product not found'}, 404
        return ProductModel.json_all(ProductModel.find_all())

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

    def delete(self, id=None):
        if not id:
            return {'error': 'URL not found on this server'}, 404
        from api.models.product import Product as ProductModel
        product = ProductModel.find_by_id(id=id)
        if not product:
            return {'error': 'Product not found'}, 404
        product.delete_from_db()
        return {'message': 'successfully deleted product'}
