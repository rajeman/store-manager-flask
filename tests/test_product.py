import json
from tests.base import BaseTestCase, CommonTestCases
from fixtures.product_fixtures import (
    create_product_valid_data,
    create_product_invalid_name,
    create_product_invalid_price,
    create_product_invalid_quantity,
    create_product_invalid_minimum_inventory,
    create_product_valid_data_response,
    create_product_invalid_data_response,
    create_product_unauthorized,
    create_product_no_json_data_expected_response,
    get_product_list_response,
    get_single_product_response,
    get_single_product_error,
    update_product_valid_data_response,
    delete_product_successful_response
)

product_url = '/api/v1/products'


class TestProduct(BaseTestCase):

    def test_create_product_admin(self):
        """
        Test to show that a product can be successfully created by
        an admin with valid product details
        """
        CommonTestCases.admin_token_assert_equal(
            self,
            product_url,
            create_product_valid_data,
            create_product_valid_data_response)

    def test_create_product_attendant(self):
        """
        Test to show that an attendant cannot create a product
        """
        CommonTestCases.attendant_token_assert_equal(
            self,
            product_url,
            create_product_valid_data,
            create_product_unauthorized)

    def test_create_product_with_invalid_product_name(self):
        """
        Test to show that a product cannot be created with product name less
        than three characters
        """
        CommonTestCases.admin_token_assert_equal(
            self,
            product_url,
            create_product_invalid_name,
            create_product_invalid_data_response)

    def test_create_product_with_invalid_product_quantity(self):
        """
        Test to show that a product cannot be created with product quantity a
        non positive integer
        """
        CommonTestCases.admin_token_assert_equal(
            self,
            product_url,
            create_product_invalid_quantity,
            create_product_invalid_data_response)

    def test_create_product_with_invalid_product_price(self):
        """
        Test to show that a product cannot be created with product price a
        non positive integer
        """
        CommonTestCases.admin_token_assert_equal(
            self,
            product_url,
            create_product_invalid_price,
            create_product_invalid_data_response)

    def test_create_product_with_invalid_minimum_inventory(self):
        """
        Test to show that a product cannot be created with minimum inventory a
        non positive integer
        """
        CommonTestCases.admin_token_assert_equal(
            self,
            product_url,
            create_product_invalid_minimum_inventory,
            create_product_invalid_data_response)

    def test_create_product_no_json_data(self):
        """
        Test to show that a user cannot be created if detail is not
        sent in JSON format
        """
        response = self.client.post(
            product_url, headers={'Authorization': 'Bearer {}'.format(self.admin_token)})
        data = json.loads(response.get_data())
        assert data == create_product_no_json_data_expected_response

    def test_get_product_list(self):
        """
        Test to show that a user can get list of products
        """
        CommonTestCases.admin_token_assert_count_equal(
            self,
            product_url,
            get_product_list_response)

    def test_get_single_product(self):
        """
        Test to show that a user can get a single product
        """
        CommonTestCases.admin_token_assert_count_equal(
            self,
            product_url+'/'+str(1),
            get_single_product_response)

    def test_get_single_product_invalid_id(self):
        """
        Test to show that a user will recieve 404 error if invalid product_id is
                                supplied
        """
        CommonTestCases.admin_token_assert_count_equal(
            self,
            product_url+'/'+str(20),
            get_single_product_error)

    def test_create_product_id_params(self):
        """
        Test to show that a product cannot be created if an id is supplied
        """
        response = self.client.post('/api/v1/products/1', data=json.dumps(
            create_product_valid_data), content_type='application/json', headers={'Authorization': 'Bearer {}'.format(self.admin_token)})
        self.assert_404(response)

    def test_update_product_valid_data(self):
        """
        Test to show that a product can be updated with valid data
        """
        CommonTestCases.admin_token_assert_put_equal(
            self,
            product_url+'/'+str(1),
            create_product_valid_data,
            update_product_valid_data_response)

    def test_update_product_no_id_params(self):
        """
        Test to show that a product cannot be updated if no id is supplied
        """
        response = self.client.put('/api/v1/products', data=json.dumps(
            create_product_valid_data), content_type='application/json', headers={'Authorization': 'Bearer {}'.format(self.admin_token)})
        self.assert_404(response)

    def test_update_product_with_invalid_data(self):
        """
        Test to show that a product cannot be updated with invalid data
        """
        CommonTestCases.admin_token_assert_put_equal(
            self,
            product_url+'/'+str(1),
            create_product_invalid_name,
            create_product_invalid_data_response)

    def test_update_product_non_existent_id(self):
        """
        Test to show that a product cannot be updated if id does not exist
        """
        response = self.client.put('/api/v1/products/-10', data=json.dumps(
            create_product_valid_data), content_type='application/json', headers={'Authorization': 'Bearer {}'.format(self.admin_token)})
        self.assert_404(response)

    def test_delete_product_non_existent_id(self):
        """
        Test to show that a product cannot be deleted if id does not exist
        """
        response = self.client.delete(
            '/api/v1/products/-10', headers={'Authorization': 'Bearer {}'.format(self.admin_token)})
        self.assert_404(response)

    def test_delete_product_no_id_params(self):
        """
        Test to show that a product cannot be deleted if no id is supplied
        """
        response = self.client.delete(
            '/api/v1/products', headers={'Authorization': 'Bearer {}'.format(self.admin_token)})
        self.assert_404(response)

    def test_delete_product_successful_data(self):
        """
        Test to show that a user can delete a product
        """
        response = self.client.delete('/api/v1/products/2', headers={
            'Authorization': 'Bearer {}'.format(self.admin_token)})
        data = json.loads(response.get_data())
        assert data == delete_product_successful_response
