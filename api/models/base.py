import datetime
from app import db


class BaseModel(db.Model):
    """Base data model for all objects"""
    __abstract__ = True

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def find_all(cls):
        return cls.query.all()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    def save_without_commit(self):
        db.session.add(self)
