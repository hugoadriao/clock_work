from flask_restx import Api

from config.app_config import app

api = Api(
    app,
    version='1.0',
    title='Work Time Checker API',
    description=(
        'The main focus of this API is build, share and create knowledge '
        'and create a API to register and monitor some work time status'
    ),
    prefix='/clock-work',
    doc='/clock-work/api'
)
