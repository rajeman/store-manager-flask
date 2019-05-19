import json
from tests.base import BaseTestCase, CommonTestCases
from fixtures.user_fixtures import (
    create_user_valid_data,
    create_user_duplicate_email,
    create_user_duplicate_email_response,
    create_user_expected_response,
    create_user_invalid_email,
    create_user_invalid_name,
    create_user_invalid_detail_response,
    create_user_no_json_data_expected_response
)

user_url = '/api/v1/auth/signup'


class TestUser(BaseTestCase):

    def test_create_user(self):
        """
        Test to show that an admin can create a user with valid user details
        """
        CommonTestCases.admin_token_assert_equal(
            self,
            user_url,
            create_user_valid_data,
            create_user_expected_response)

    def test_create_user_email_in_use(self):
        """
        Test to show that a user cannot be created if email is in use
        """
        CommonTestCases.admin_token_assert_equal(
            self,
            user_url,
            create_user_duplicate_email,
            create_user_duplicate_email_response)

    def test_create_user_no_json_data(self):
        """
        Test to show that a user cannot be created if detail is not
        sent in JSON format
        """
        response = self.client.post(
            '/api/v1/auth/signup', headers={'Authorization': 'Bearer {}'.format(self.admin_token)})
        data = json.loads(response.get_data())
        assert data == create_user_no_json_data_expected_response

    def test_create_user_invalid_name(self):
        """
        Test to show that a user cannot be created if name is invalid
        """
        CommonTestCases.admin_token_assert_equal(
            self,
            user_url,
            create_user_invalid_name,
            create_user_invalid_detail_response)

    def test_create_user_invalid_email(self):
        """
        Test to show that a user cannot be created if email is invalid
        """
        CommonTestCases.admin_token_assert_equal(
            self,
            user_url,
            create_user_invalid_email,
            create_user_invalid_detail_response)
