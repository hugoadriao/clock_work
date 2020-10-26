from config.app_config import app


if __name__ == '__main__':
    from config.sql_alchemy import db

    db.init_app(app)
    app.run(host='0.0.0.0', port=5000, debug=True)
