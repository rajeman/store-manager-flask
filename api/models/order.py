from sqlalchemy import (Column, Integer, BigInteger, Text, ForeignKey)
from sqlalchemy.orm import relationship
from api.models.base import BaseModel
from app import db

class Order(BaseModel):
    __tablename__ = 'orders'
    id = Column(Integer,  primary_key=True,)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    time_checked_out = Column(BigInteger, nullable=False)
    product_price = Column(Integer, nullable=False)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    product_quantity = Column(Integer, nullable=False)
    user = relationship("User", backref="order")
