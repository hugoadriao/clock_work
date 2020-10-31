from config.app_config import app
from namespace import *
from resources.clock import Clock


clock_namespace.add_resource(
    Clock,
    '/clocks',
    route_doc={
        'description': 'This route returns hello world',
        'responses': {
            404: "Not found",
            200: "Success",
            500: "Internal Error"
        }
    }
)

# TODO delete this when the application is ready
from config.sql_alchemy import db

db.init_app(app)
# only to debug with PyCharm

if __name__ == '__main__':
    from config.sql_alchemy import db

    db.init_app(app)
    app.run(host='0.0.0.0', port=5000, debug=True)
