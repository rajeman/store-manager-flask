import json
from tests.base import BaseTestCase, CommonTestCases
from fixtures.order_fixtures import (
    create_order_valid_order_details,
    expected_response_valid_order_details,
    create_order_empty_products_array,
    expected_response_empty_products_array,
    create_order_products_array_containing_non_dict,
    expected_response_product_array_non_dict_item,
    create_order_product_id_invalid,
    expected_response_invalid_product_id,
    create_order_product_quantity_invalid,
    expected_response_invalid_product_quantity,
    create_order_non_existing_product,
    expected_response_non_existing_product,
    create_order_not_enough_product,
    expected_response_not_enough_product,
    create_order_duplicate_product_id,
    expected_response_duplicate_product_id,
    expected_response_create_order_no_json_data,
    expected_response_get_order_list,
    expected_response_get_order_details,
    expected_response_get_order_details_different_attendant,
    expected_response_get_order_details_invalid_timestamp,
    expected_response_get_order_details_non_existing_order
)

order_url = '/api/v1/sales'


class TestOrder(BaseTestCase):

    def test_create_order_attendant(self):
        """
        Test to show that an order can be successfully created by
        an attendant with valid product details
        """
        response = self.client.post(order_url, data=json.dumps(
            create_order_valid_order_details), content_type='application/json',
            headers={'Authorization': 'Bearer {}'.format(self.attendant_token)})
        data = json.loads(response.get_data())
        self.assertCountEqual(expected_response_valid_order_details, data)

    def test_create_order_invalid_products_array(self):
        """
        Test to show that an order cannot be created if products
        array is invalid
        """
        CommonTestCases.attendant_token_assert_equal(
            self,
            order_url,
            create_order_empty_products_array,
            expected_response_empty_products_array)

    def test_create_order_products_array_non_dict_item(self):
        """
        Test to show that an order cannot be created if products
        array has non dict item
        """
        CommonTestCases.attendant_token_assert_equal(
            self,
            order_url,
            create_order_products_array_containing_non_dict,
            expected_response_product_array_non_dict_item)

    def test_create_order_product_id_invalid(self):
        """
        Test to show that an order cannot be created if supplied productId
        is invalid
        """
        CommonTestCases.attendant_token_assert_equal(
            self,
            order_url,
            create_order_product_id_invalid,
            expected_response_invalid_product_id)

    def test_create_order_product_quantity_invalid(self):
        """
        Test to show that an order cannot be created if supplied productQuantity
        is invalid
        """
        CommonTestCases.attendant_token_assert_equal(
            self,
            order_url,
            create_order_product_quantity_invalid,
            expected_response_invalid_product_quantity)

    def test_create_order_non_existing_product(self):
        """
        Test to show that an order cannot be created if supplied product does
        not exist
        """
        CommonTestCases.attendant_token_assert_equal(
            self,
            order_url,
            create_order_non_existing_product,
            expected_response_non_existing_product)

    def test_create_order_not_enough_product(self):
        """
        Test to show that an order cannot be created if supplied product is
        greater than available product
        """
        CommonTestCases.attendant_token_assert_equal(
            self,
            order_url,
            create_order_not_enough_product,
            expected_response_not_enough_product)

    def test_create_order_duplicate_product_id(self):
        """
        Test to show that an order cannot be created if productId is duplicate
        """
        CommonTestCases.attendant_token_assert_equal(
            self,
            order_url,
            create_order_duplicate_product_id,
            expected_response_duplicate_product_id)

    def test_create_order_no_json_data(self):
        """
        Test to show that an order cannot be created if details is not
        sent in JSON format
        """
        response = self.client.post(order_url,
            headers={'Authorization': 'Bearer {}'.format(self.attendant_token)})
        data = json.loads(response.get_data())
        assert data == expected_response_create_order_no_json_data

    def test_get_order_list_admin(self):
            """
            Test to show that an admin can get list of orders
            """
            CommonTestCases.admin_token_assert_count_equal(
                self,
                order_url,
                expected_response_get_order_list)

    def test_get_order_list_attendant(self):
            """
            Test to show that an attendant can get list of orders made by her
            """
            CommonTestCases.attendant_token_assert_count_equal(
                self,
                order_url,
                expected_response_get_order_list)

    def test_get_order_details_admin(self):
            """
            Test to show that an admin can get the details of an order
            """
            CommonTestCases.admin_token_assert_count_equal(
                self,
                order_url + '/1558902658490',
                expected_response_get_order_details)

    def test_get_order_details_attendant(self):
            """
            Test to show that an attendant can get the details of an order
            he created
            """
            CommonTestCases.attendant_token_assert_count_equal(
                self,
                order_url + '/1558902658490',
                expected_response_get_order_details)

    def test_get_order_details_different_attendant(self):
            """
            Test to show that an attendant cannot get the details of an order
            he didn't make
            """
            CommonTestCases.attendant_token_2_assert_count_equal(
                self,
                order_url + '/1558902658490',
                expected_response_get_order_details_different_attendant)

    def test_get_order_details_invalid_timestamp(self):
            """
            Test to show that an order details cannot be gotten if the timestamp
            params is not a valid integer
            """
            CommonTestCases.attendant_token_assert_count_equal(
                self,
                order_url + '/15589026584901223987989287879287987',
                expected_response_get_order_details_invalid_timestamp)

    def test_get_order_details_non_existent_timestamp_params(self):
            """
            Test to show that an order details cannot be gotten if the supplied
            timestamp is not existent
            """
            CommonTestCases.attendant_token_assert_count_equal(
                self,
                order_url + '/15589026',
                expected_response_non_existing_product)
