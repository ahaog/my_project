from datetime import datetime
import sqlalchemy.orm as dec
import sqlalchemy as sa
from sqlalchemy import orm

SqlAlchemyBase = dec.declarative_base()

conn_str = f'sqlite:///statistics_of_students?check_same_thread=False'

engine = sa.create_engine(conn_str, echo=False)


class Students(SqlAlchemyBase):
    __tablename__ = "students"
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.Text)

    stat = orm.relationship("Statistics", backref="students", uselist=False)


class Statistics(SqlAlchemyBase):
    __tablename__ = "statistics"
    id = sa.Column(sa.Integer, primary_key=True)
    speed = sa.Column(sa.Float, nullable=True)
    authenticity = sa.Column(sa.Float, nullable=True)
    last_entry_time = sa.Column(sa.DateTime, default=datetime.now)
    print_language = sa.Column(sa.String(3), nullable=True)

    user_id = sa.Column(sa.Integer, sa.ForeignKey("students.id"), autoincrement=True)


if __name__ == '__main__':
    SqlAlchemyBase.metadata.create_all(engine)
