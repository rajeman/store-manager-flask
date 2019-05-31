create_order_valid_order_details = {
	"products": [{"productId": 1, "productQuantity": 10}]
}

expected_response_valid_order_details = {
    "message": "Successfully created order",
    "orderDetails": {
        "user_id": 1,
        "order_price": 30,
        "order_quantity": 10
    }
}

create_order_empty_products_array = {
	"products": []
}

expected_response_empty_products_array = {
    "error": "products array not provided or empty"
}

create_order_products_array_containing_non_dict = {
	"products": [1, 2, 3]
}

expected_response_product_array_non_dict_item = {
    "error": "products array item is not an object"
}

create_order_product_id_invalid = {
	"products": [{"productId": -10}]
}

expected_response_invalid_product_id = {
    "error": "productId must be supplied as a positive integer"
}

create_order_product_quantity_invalid = {
	"products": [{"productId": 1}, {"productQuantity": "thirty eight"}]
}

expected_response_invalid_product_quantity = {
    "error": "productQuantity must be supplied as a positive integer"
}

create_order_non_existing_product = {
	"products": [{"productId": 10, "productQuantity": 10}]
}

expected_response_non_existing_product = {
    "error": "product with id 10 does not exit"
}

create_order_not_enough_product = {
	"products": [{"productId": 1, "productQuantity": 2000}]
}

expected_response_not_enough_product = {
    "error": "quantity \"2000\" supplied for \"Wifi Module\" with id \"1\" is greater than available quantity \"1015\""
}

create_order_duplicate_product_id = {
	"products": [{"productId": 1, "productQuantity": 5}, {"productId": 1, "productQuantity": 10}]
}

expected_response_duplicate_product_id = {
    "error": "product with id \"1\" is supplied twice"
}


expected_response_create_order_no_json_data = {
    'msg': 'Missing JSON in request'
}

expected_response_get_order_list = {
    'message': 'successfully fetched orders',
    'orders': [
        {
            "order_id": 1,
            "user_id": 1,
            "user_name": "Susan Nice",
            "time_checked_out": 1558902658490,
            "order_price": 575,
            "order_quantity": 25
        },
        {
            "order_id": 3,
            "user_id": 1,
            "user_name": "Susan Nice",
            "time_checked_out": 1558902658499,
            "order_price": 132,
            "order_quantity": 11
        }
    ]
}

expected_response_get_order_details = {
 "message": "successfully fetched order",
    "orderDetails": [
        {
            "user_id": 1,
            "time_checked_out": 1558902813830,
            "product_name": "Wifi Module",
            "product_price": 20,
            "product_quantity": 10,
            "product_id": 1,
            "total_price": 200,
            "user_name": "Susan Nice"
        },
        {
            "user_id": 8,
            "time_checked_out": 1558902813830,
            "product_name": "Raspberry Pi",
            "product_price": 25,
            "product_quantity": 15,
            "product_id": 2,
            "total_price": 375,
            "user_name": "Susan Nice"
        }
    ]
}

expected_response_get_order_details_different_attendant = {
    "error": "You are not authorized to view this order"
}

expected_response_get_order_details_invalid_timestamp = {
    "error": "invalid order timestamp"
}

expected_response_get_order_details_non_existing_order = {
    "error": "order not found"
}
