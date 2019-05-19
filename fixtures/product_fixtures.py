create_product_valid_data = {
    "productName": "Raspberry Pi",
    "productQuantity": 40,
    "price": 5,
    "minimumInventory": 1
}

create_product_unauthorized = {
    "error": "You are not authorized to perform this action"
}

create_product_valid_data_response = {
    "message": "Raspberry Pi was successfully added"
}

create_product_invalid_data_response = {
    "error": "Invalid product input. Product name must be at least 3 characters with product price, product quantity and minimum inventory positive integers"
}

create_product_invalid_name = {
    "productName": "Ra",
    "productQuantity": 40,
    "price": 5,
    "minimumInventory": 1
}

create_product_invalid_quantity = {
    "productName": "Arduino",
    "productQuantity": -1,
    "price": 5,
    "minimumInventory": 1
}

create_product_invalid_price = {
    "productName": "Arduino",
    "productQuantity": 20,
    "price": 0,
    "minimumInventory": 1
}

create_product_invalid_minimum_inventory = {
    "productName": "Arduino",
    "productQuantity": 20,
    "price": 12,
    "minimumInventory": -1
}

create_product_no_json_data_expected_response = {
    'msg': 'Missing JSON in request'
}

get_product_list_response = [
    {
        "product_id": 1,
        "product_name": "Wifi Module",
        "product_quantity": 1015,
        "product_price": 30,
        "minimum_inventory": 5
    },
    {
        "product_id": 2,
        "product_name": "RFID Reader",
        "product_quantity": 100,
        "product_price": 12,
        "minimum_inventory": 15
    }
]

get_single_product_response = [
    {
        "product_id": 1,
        "product_name": "Wifi Module",
        "product_quantity": 1015,
        "product_price": 30,
        "minimum_inventory": 5
    }
]

get_single_product_error = {'error': 'Product not found'}

update_product_valid_data_response = {
    "message": "successfully updated product"
}

delete_product_successful_response = {
    "message": "successfully deleted product"
}
