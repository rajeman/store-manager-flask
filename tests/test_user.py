import json
from tests.base import BaseTestCase
from fixtures.user_fixtures import (
    create_user_valid_data,
    create_user_duplicate_email,
    create_user_duplicate_email_response,
    create_user_expected_response,
    create_user_invalid_email,
    create_user_invalid_name,
    create_user_invalid_detail_response
)


class TestUser(BaseTestCase):

    def test_create_user(self):
        """
        Test to show that a user can be created with valid user details
        """
        response = self.client.post('/api/v1/auth', data=json.dumps(
            create_user_valid_data), content_type='application/json')
        data = json.loads(response.get_data())
        assert data == create_user_expected_response

    def test_create_user_email_in_use(self):
        """
        Test to show that a user cannot be created if email is in use
        """
        response = self.client.post('/api/v1/auth', data=json.dumps(
            create_user_duplicate_email), content_type='application/json')
        data = json.loads(response.get_data())
        assert data == create_user_duplicate_email_response

    def test_create_user_invalid_name(self):
        """
        Test to show that a user cannot be created if name is invalid
        """
        response = self.client.post(
            '/api/v1/auth', data=json.dumps(create_user_invalid_name),
            content_type='application/json')
        data = json.loads(response.get_data())
        assert data == create_user_invalid_detail_response

    def test_create_user_invalid_email(self):
        """
        Test to show that a user cannot be created if email is invalid
        """
        response = self.client.post(
            '/api/v1/auth', data=json.dumps(create_user_invalid_email),
            content_type='application/json')
        data = json.loads(response.get_data())
        assert data == create_user_invalid_detail_response
