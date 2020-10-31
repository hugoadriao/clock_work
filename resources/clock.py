from datetime import datetime, timedelta, time

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

        max_no_break_time = None
        worked_time = None
        close_of_business = None
        extra_hour = None

        if len(all_model_registers) == 1:
            max_no_break_time = (
                    all_model_registers[0].cloregister + timedelta(
                        hours=6
                    )
            )
        elif len(all_model_registers) == 2:

            worked_time = (
                    all_model_registers[1].cloregister -
                    all_model_registers[0].cloregister
            )

        all_datetime_registers: [str] = [
            str(validate_date(register.cloregister)) for register in
            all_model_registers
        ]

        return all_datetime_registers
