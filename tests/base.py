from flask_testing import TestCase
import json
from app import app, db
from api.models.product import Product as ProductModel
from api.models.user import User as UserModel
from fixtures.auth_fixtures import (
    login_user_valid_data as login_attendant_valid_data,
    login_admin_valid_data)


class BaseTestCase(TestCase):

    def create_app(self):
        return app

    def setUp(self):
        self.test_app = self.create_app()
        with self.test_app.app_context():
            db.create_all()
            product_1 = ProductModel(name='Wifi Module',
                                     price=30,
                                     minimum_inventory=5,
                                     quantity=1015)
            product_2 = ProductModel(name='RFID Reader',
                                     price=12,
                                     minimum_inventory=15,
                                     quantity=100)
            db.session.add(product_1)
            db.session.add(product_2)
            attendant = UserModel(name='Susan Nice', email='suzan.nice@hoc.com',
                                  password='$2b$12$Xl7npipxV3ejaaIGRKNp1uotTK5Gi0ka6t312mhyRYv1qgXV9UOMe',
                                  level=1
                                  )
            db.session.add(attendant)
            admin = UserModel(name='Gregory Best', email='gregory.best@hoc.com',
                              password='$2b$12$Xl7npipxV3ejaaIGRKNp1uotTK5Gi0ka6t312mhyRYv1qgXV9UOMe',
                              level=2
                              )
            db.session.add(admin)
            db.session.commit()
        response = self.test_app.test_client().post('/api/v1/auth/login', data=json.dumps(
            login_admin_valid_data), content_type='application/json')
        data = json.loads(response.get_data())
        self.admin_token = data['token']
        response = self.test_app.test_client().post('/api/v1/auth/login', data=json.dumps(
            login_attendant_valid_data), content_type='application/json')
        data = json.loads(response.get_data())
        self.attendant_token = data['token']
        self.client = self.test_app.test_client()

    def tearDown(self):
        with self.test_app.app_context():
            db.session.close()
            db.drop_all()


class CommonTestCases(BaseTestCase):

    def admin_token_assert_equal(self, url, json_data, expected_response):
        response = self.client.post(url, data=json.dumps(
            json_data), content_type='application/json', headers={'Authorization': 'Bearer {}'.format(self.admin_token)})
        data = json.loads(response.get_data())
        assert data == expected_response

    def admin_token_assert_count_equal(self, url, expected_response):
        response = self.client.get(url, content_type='application/json',
                                   headers={'Authorization': 'Bearer {}'.format(self.admin_token)})
        data = json.loads(response.get_data())
        self.assertCountEqual(data, expected_response)

    def admin_token_assert_put_equal(self, url, json_data, expected_response):
        response = self.client.put(url, data=json.dumps(
            json_data), content_type='application/json', headers={'Authorization': 'Bearer {}'.format(self.admin_token)})
        data = json.loads(response.get_data())
        assert data == expected_response

    def attendant_token_assert_equal(self, url, json_data, expected_response):
        response = self.client.post(url, data=json.dumps(
            json_data), content_type='application/json', headers={'Authorization': 'Bearer {}'.format(self.attendant_token)})
        data = json.loads(response.get_data())
        assert data == expected_response
