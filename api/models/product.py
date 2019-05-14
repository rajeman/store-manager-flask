from sqlalchemy import (Column, Integer, Text)
from api.models.base import BaseModel


class Product(BaseModel):
    __tablename__ = 'products'
    id = Column(Integer,  primary_key=True,)
    name = Column(Text, nullable=False)
    minimum_inventory = Column(Integer, default=0)
    price = Column(Integer, nullable=False)
    quantity = Column(Integer, nullable=False)

    def json(self):
        return [{'product_id': self.id,
                 'product_name': self.name,
                 'product_price': self.price,
                 'product_quantity': self.quantity,
                 'minimum_inventory': self.minimum_inventory}]

    @classmethod
    def json_all(cls, products):
        return [{'product_id': product.id,
                 'product_name': product.name,
                 'product_price': product.price,
                 'product_quantity': product.quantity,
                 'minimum_inventory': product.minimum_inventory}
                for product in products]
