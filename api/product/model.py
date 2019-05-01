from sqlalchemy import (Column, Integer, Text)
from api.model import BaseModel


class Products(BaseModel):
    __tablename__ = 'products'
    id = Column(Integer,  primary_key=True,)
    name = Column(Text, nullable=False)
    minimum_inventory = Column(Integer, default=0)
    price = Column(Integer, nullable=False)
    quantity = Column(Integer, nullable=False)
