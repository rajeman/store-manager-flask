import json
from tests.base import BaseTestCase
from fixtures.product_fixtures import (
    create_product_valid_data,
    create_product_invalid_name,
    create_product_invalid_price,
    create_product_invalid_quantity,
    create_product_invalid_minimum_inventory,
    create_product_valid_data_response,
    create_product_invalid_data_response,
    get_product_list_response,
    get_single_product_response,
    get_single_product_error,
    update_product_valid_data_response
)


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
            '/api/v1/products', data=json.dumps(create_product_invalid_name),
            content_type='application/json')
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

    def test_get_product_list(self):
        """
        Test to show that a user can get list of products
        """
        response = self.client.get('/api/v1/products')
        data = json.loads(response.get_data())
        self.assertCountEqual(data, get_product_list_response)

    def test_get_single_product(self):
        """
        Test to show that a user can get a single product
        """
        response = self.client.get('/api/v1/products/1')
        data = json.loads(response.get_data())
        self.assertCountEqual(data, get_single_product_response)

    def test_get_single_product_invalid_id(self):
        """
        Test to show that a user will recieve 404 error if invalid product_id is
                                supplied
        """
        response = self.client.get('/api/v1/products/10')
        data = json.loads(response.get_data())
        self.assertCountEqual(data, get_single_product_error)

    def test_create_product_id_params(self):
        """
        Test to show that a product cannot be created if an id is supplied
        """
        response = self.client.post('/api/v1/products/1', data=json.dumps(
            create_product_valid_data), content_type='application/json')
        self.assert_404(response)

    def test_update_product_valid_data(self):
        """
        Test to show that a product can be updated with valid data
        """
        response = self.client.put('/api/v1/products/1', data=json.dumps(
            create_product_valid_data), content_type='application/json')
        data = json.loads(response.get_data())
        assert data == update_product_valid_data_response

    def test_update_product_no_id_params(self):
        """
        Test to show that a product cannot be updated if no id is supplied
        """
        response = self.client.put('/api/v1/products', data=json.dumps(
            create_product_valid_data), content_type='application/json')
        self.assert_404(response)

    def test_update_product_with_invalid_data(self):
        """
        Test to show that a product cannot be updated with invalid data
        """
        response = self.client.post(
            '/api/v1/products/1', data=json.dumps(create_product_invalid_name),
            content_type='application/json')
        data = json.loads(response.get_data())
        assert data == create_product_invalid_data_response

    def test_update_product_non_existent_id(self):
        """
        Test to show that a product cannot be updated if id does not exist
        """
        response = self.client.put('/api/v1/products/-10', data=json.dumps(
            create_product_valid_data), content_type='application/json')
        self.assert_404(response)
