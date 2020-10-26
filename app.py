from config.app_config import app


@app.before_first_request
def create_database():
    db.create_all()


if __name__ == '__main__':
    from config.sql_alchemy import db

    db.init_app(app)
    app.run(host='0.0.0.0', port=5000, debug=True)
