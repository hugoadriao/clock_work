from flask_restx import Resource


class Clock(Resource):

    def get(self):
        return 'hello world'
