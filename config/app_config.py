from flask import Flask

from config.db_config import SQLITE_URI


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = SQLITE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
