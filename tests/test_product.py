import json
from tests.base import BaseTestCase
from fixtures.product_fixtures import (
    create_product_valid_data,
    create_product_invalid_name,
    create_product_invalid_price,
    create_product_invalid_quantity,
    create_product_invalid_minimum_inventory,
    create_product_valid_data_response,
    create_product_invalid_data_response)


class TestProduct(BaseTestCase):
    def test_create_product(self):
        """
        Test to show that a product can be successfully created with valid
                                details
        """
        response = self.client.post('/api/v1/products', data=json.dumps(
            create_product_valid_data), content_type='application/json')
        data = json.loads(response.get_data())
        assert data == create_product_valid_data_response

    def test_create_product_with_invalid_product_name(self):
        """
        Test to show that a product cannot be created with product name less
        than three characters
        """
        response = self.client.post(
            '/api/v1/products', data=json.dumps(create_product_invalid_name), content_type='application/json')
        data = json.loads(response.get_data())
        assert data == create_product_invalid_data_response

    def test_create_product_with_invalid_product_quantity(self):
        """
        Test to show that a product cannot be created with product quantity a
        non positive integer
        """
        response = self.client.post('/api/v1/products', data=json.dumps(
            create_product_invalid_quantity), content_type='application/json')
        data = json.loads(response.get_data())
        assert data == create_product_invalid_data_response

    def test_create_product_with_invalid_product_price(self):
        """
        Test to show that a product cannot be created with product price a
        non positive integer
        """
        response = self.client.post('/api/v1/products', data=json.dumps(
            create_product_invalid_price), content_type='application/json')
        data = json.loads(response.get_data())
        assert data == create_product_invalid_data_response

    def test_create_product_with_invalid_minimum_inventory(self):
        """
        Test to show that a product cannot be created with minimum inventory a
        non positive integer
        """
        response = self.client.post('/api/v1/products', data=json.dumps(
            create_product_invalid_minimum_inventory), content_type='application/json')
        data = json.loads(response.get_data())
        assert data == create_product_invalid_data_response
