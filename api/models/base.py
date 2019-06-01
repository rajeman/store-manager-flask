import datetime
from app import db


class BaseModel(db.Model):
    """Base data model for all objects"""
    __abstract__ = True

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def save_without_commit(self):
        db.session.add(self)
