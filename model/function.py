from config.sql_alchemy import db


class FunctionModel(db.Model):
    __tablename__ = 'function'

    funid = db.Column(
        db.Integer,
        primary_key=True,
        server_default=db.FetchedValue()
    )
    fundescription = db.Column(db.String(40), nullable=False)
