from sqlalchemy import (Column, Integer, Text, Index)
from api.models.base import BaseModel


class User(BaseModel):
    __tablename__ = 'users'
    id = Column(Integer,  primary_key=True,)
    name = Column(Text, nullable=False)
    email = Column(Text, nullable=False)
    password = Column(Text, nullable=False)
    total_orders = Column(Integer, default=0)
    level = Column(Integer, nullable=False)

    __table_args__ = (
            Index(
                'ix_unique_email_content',
                'email',
                unique=True
                ),
        )

    @classmethod
    def find_by_email(cls, email):
        return cls.query.filter_by(email=email).first()
