from datetime import datetime

from flask_restx import Resource

from model.clock import ClockModel
from utils.generic_functions import validate_date


class Clock(Resource):

    def get(self):
        user_id = 2
        date_now = datetime.now()
        all_model_registers: [ClockModel] = (
            ClockModel.get_all_registers_from_today(date_now, user_id)
        )

        all_datetime_registers: [str] = [
            str(validate_date(register.cloregister)) for register in
            all_model_registers
        ]

        return all_datetime_registers
