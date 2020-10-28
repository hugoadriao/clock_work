from config.sql_alchemy import db


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
        'Person',
        primaryjoin='ClockModel.cloperid == Person.perid',
        backref='clocks'
    )
