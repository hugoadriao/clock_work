from config.sql_alchemy import db
from model.function import FunctionModel


class PersonModel(db.Model):
    __tablename__ = 'person'

    perid = db.Column(
        db.Integer,
        primary_key=True,
        server_default=db.FetchedValue()
    )
    peractive = db.Column(
        db.Boolean,
        nullable=False,
        server_default=db.FetchedValue()
    )
    perfunction = db.Column(
        db.ForeignKey('function.funid', ondelete='SET NULL')
    )
    persupervisor = db.Column(db.Integer)
    perworktime = db.Column(db.Time, nullable=False)
    perhourbank = db.Column(db.Time, server_default=db.FetchedValue())
    pername = db.Column(db.String(40), nullable=False)
    percode = db.Column(db.String(30))

    function_relation = db.relationship(
        FunctionModel,
        primaryjoin='PersonModel.perfunction == FunctionModel.funid',
        backref='people'
    )
