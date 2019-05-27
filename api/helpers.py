from flask_restful import abort
import functools
import re
from flask_jwt_extended import get_jwt_identity

Attendant = 1
Admin = 2


def valid_product(request):
    def valid_product_decorator(func):
        @functools.wraps(func)
        def wrapper(self, id=None):
            kwargs = request.get_json()
            if not kwargs:
                return {"msg": "Missing JSON in request"}, 400
            name = kwargs.get('productName')
            quantity = kwargs.get('productQuantity')
            price = kwargs.get('price')
            minimum_inventory = kwargs.get('minimumInventory')
            is_valid = name and len(str(name)) > 2 and price and \
                str(price).isdigit() and minimum_inventory and \
                str(minimum_inventory).isdigit() and quantity and \
                str(quantity).isdigit()
            if is_valid:
                return func(self, id)
            return {'error': ('Invalid product input. Product name must be at '
                              'least 3 characters with product price, product quantity and '
                              'minimum inventory positive integers')}, 422
        return wrapper
    return valid_product_decorator


def valid_user_details(request):
    def valid_user_details_decorator(func):
        @functools.wraps(func)
        def wrapper(self, id=None):
            kwargs = request.get_json()
            if not kwargs:
                return {"msg": "Missing JSON in request"}, 400
            email = kwargs.get('email', '')
            name = kwargs.get('name', '')
            is_valid = re.search(
                r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)', email) and len(str(name)) > 2
            if is_valid:
                return func(self, id)
            return {'error': ('Invalid input. Make sure email is valid and name is at least 3 characters')}, 400
        return wrapper
    return valid_user_details_decorator


def user_level(*levels):
    def allowed_levels(func):
        @functools.wraps(func)
        def wrapper(self, id=None):
            from api.models.user import User as UserModel
            current_user = get_jwt_identity()
            if current_user['level'] not in levels or not UserModel.query.get(current_user['id']):
                return {"error": "You are not authorized to perform this action"}, 401
            return func(self, id)
        return wrapper
    return allowed_levels


def update_entity_fields(entity, **kwargs):
    keys = kwargs.keys()
    for key in keys:
        exec("entity.{0} = kwargs['{0}']".format(key))
    return entity

def valid_order_items(request):
        def valid_order_items_decorator(func):
            @functools.wraps(func)
            def wrapper(self, id=None):
                kwargs = request.get_json()
                if not kwargs:
                    return {"msg": "Missing JSON in request"}, 400
                order_items = kwargs.get('products')
                if not isinstance(order_items, list) or len(order_items) < 1:
                    return {"error": "products array not provided or empty"}
                validate_order_items(order_items)
                return func(self, id)
            return wrapper
        return valid_order_items_decorator

def validate_order_items(order_items):
    from api.models.product import Product as ProductModel
    vetted_order_items = {}
    for product in order_items:
        if not isinstance(product, dict):
            abort(400, error='products array item is not an object')
        product_id = product.get('productId')
        product_quantity = product.get('productQuantity')
        if not (product_id and isinstance(product_id, int)  and product_id > 0):
            abort(400, error='productId must be supplied as a positive integer')
        if not (product_quantity and isinstance(product_quantity, int) and product_quantity > 0):
            abort(400, error='productQuantity must be supplied as a positive integer')
        actual_product = ProductModel.find_by_id(product_id)
        if not actual_product:
            abort(400, error='product with id {} does not exit'.format(product_id))
        if product_quantity > actual_product.quantity:
            abort(400, error='quantity "{}" supplied for "{}" with id "{}" is greater than available quantity "{}"'.format(
                product_quantity, actual_product.name, product_id, actual_product.quantity))
        if vetted_order_items.get(product_id):
            abort(400, error='product with id "{}" is supplied twice'.format(product_id))
        vetted_order_items[product_id] = product_id
