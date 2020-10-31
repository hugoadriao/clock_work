from datetime import date, datetime

from config.sql_alchemy import db
from model.person import PersonModel


class ClockModel(db.Model):
    __tablename__ = 'clock'

    cloid = db.Column(
        db.Integer,
        primary_key=True,
        nullable=False,
        server_default=db.FetchedValue()
    )
    cloregister = db.Column(db.Time, nullable=False)
    clotimestamp = db.Column(
        db.DateTime,
        primary_key=True,
        nullable=False
    )
    cloperid = db.Column(
        db.ForeignKey('person.perid'),
        primary_key=True, nullable=False
    )

    person_relation = db.relationship(
        PersonModel,
        primaryjoin='ClockModel.cloperid == PersonModel.perid',
        backref='clocks'
    )

    @classmethod
    def get_all_registers_from_today(cls, date_now: date, user_id):
        date_hour_start = datetime(
            year=date_now.year,
            month=date_now.month,
            day=date_now.day,
            hour=0,
            minute=0,
            second=0
        )
        date_hour_end = datetime(
            year=date_now.year,
            month=date_now.month,
            day=date_now.day,
            hour=23,
            minute=59,
            second=59
        )
        all_registers = cls.query.filter(
            cls.cloperid == user_id,
            cls.cloregister >= date_hour_start,
            cls.cloregister <= date_hour_end
        ).order_by(cls.cloregister).all()

        return all_registers
