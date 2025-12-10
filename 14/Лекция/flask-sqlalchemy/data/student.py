import sqlalchemy
from .db_sessions import SqlAlchemyBase
from sqlalchemy import orm

class Student(SqlAlchemyBase):
    __tablename__ = 'students'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    surname = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    mark = orm.relationship("Grade", back_populates='student')