import json
from tests.base import BaseTestCase
from fixtures.auth_fixtures import (
    login_user_valid_data,
    login_user_invalid_email,
    login_user_invalid_password,
    login_user_invalid_detail_expected_response,
    login_user_no_json_data_expected_response
)


class TestUser(BaseTestCase):

    def test_login_user(self):
        """
        Test to show that a user can login with valid details
        """
        response = self.client.post('/api/v1/auth/login', data=json.dumps(
            login_user_valid_data), content_type='application/json')
        self.assert200(response)

    def test_login_user_no_json_data(self):
        """
        Test to show that a user cannot be logged in if details is not
        sent in JSON format
        """
        response = self.client.post('/api/v1/auth/login')
        data = json.loads(response.get_data())
        assert data == login_user_no_json_data_expected_response

    def test_login_user_invalid_email(self):
        """
        Test to show that a user cannot be logged in if user is not registered
        """
        response = self.client.post('/api/v1/auth/login', data=json.dumps(
            login_user_invalid_email), content_type='application/json')
        data = json.loads(response.get_data())
        assert data == login_user_invalid_detail_expected_response

    def test_login_user_invalid_password(self):
        """
        Test to show that a user cannot be logged in if user password is incorrect
        """
        response = self.client.post('/api/v1/auth/login', data=json.dumps(
            login_user_invalid_password), content_type='application/json')
        data = json.loads(response.get_data())
        assert data == login_user_invalid_detail_expected_response
