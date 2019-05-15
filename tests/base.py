from flask_testing import TestCase
from app import app, db
from api.models.product import Product as ProductModel
from api.models.user import User as UserModel


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
            user = UserModel(name='Susan Nice', email='suzan.nice@hoc.com',
                             password='$2b$12$Xl7npipxV3ejaaIGRKNp1uotTK5Gi0ka6t312mhyRYv1qgXV9UOMe',
                             level=1
                             )
            db.session.add(user)
            db.session.commit()
        self.client = self.test_app.test_client()

    def tearDown(self):
        with self.test_app.app_context():
            db.session.close()
            db.drop_all()
