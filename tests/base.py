from flask_testing import TestCase
from app import app, db
from api.models import product


class BaseTestCase(TestCase):

    def create_app(self):
        return app

    def setUp(self):
        self.test_app = self.create_app()
        with self.test_app.app_context():
            db.create_all()
        self.client = self.test_app.test_client()

    def tearDown(self):
        with self.test_app.app_context():
            db.drop_all()
