import sqlalchemy
from .db_sessions import SqlAlchemyBase
from sqlalchemy import orm

class Grade(SqlAlchemyBase):
    __tablename__ = 'grade'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    student_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("students.id"))
    mark = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    student = orm.relationship('Student')