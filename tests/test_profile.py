import json
from tests.base import BaseTestCase, CommonTestCases
from fixtures.profile_fixtures import expected_response_get_user_details

profile_url = '/api/v1/user'


class TestProfile(BaseTestCase):

    def test_get_user_details(self):
        """
        Test to show that a user can get the profile details
        """
        CommonTestCases.attendant_token_assert_count_equal(
            self,
            profile_url,
            expected_response_get_user_details)
