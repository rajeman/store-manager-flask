import functools


def valid_product(request):
    def valid_product_decorator(func):
        @functools.wraps(func)
        def wrapper(self, id=None):
            if id:
                return {'error': 'URL not found on this server'}, 404
            kwargs = request.get_json()
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
