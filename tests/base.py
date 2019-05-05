from flask_testing import TestCase
from app import app, db
from api.models.product import Product as ProductModel


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
            db.session.commit()
        self.client = self.test_app.test_client()

    def tearDown(self):
        with self.test_app.app_context():
            db.session.close()
            db.drop_all()