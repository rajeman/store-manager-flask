create_product_valid_data = {
    "productName": "Raspberry Pi",
    "productQuantity": 40,
    "price": 5,
    "minimumInventory": 1
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
