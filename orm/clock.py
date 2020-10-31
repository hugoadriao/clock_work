from model.clock import ClockModel


class ClockORM:
    def __init__(
            self, cloid, clotimestamp, cloperid, cloregister=None
    ):
        self.cloid = cloid
        self.clotimestamp = clotimestamp
        self.cloperid = cloperid
        self.cloregister = cloregister

    def json(self):
        cloid = self.cloid
        clotimestamp = self.clotimestamp
        cloperid = self.cloperid
        cloregister = self.cloregister

    @classmethod
    def model_to_orm(cls, model: ClockModel):
        return ClockORM(
            model.cloid,
            model.clotimestamp,
            model.cloperid,
            model.cloregister
        )
