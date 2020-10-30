SQLITE_URI = 'sqlite:///database/clock_database.db'

POSTGRESQL_CONFIG = {
    'user': 'hugo',
    'password': '1029',
    'host': 'localhost',
    'port': '5432',
    'database': 'mydb'
}
p_user = POSTGRESQL_CONFIG.get('user')
p_password = POSTGRESQL_CONFIG.get('password')
p_host = POSTGRESQL_CONFIG.get('host')
p_port = POSTGRESQL_CONFIG.get('port')
p_database = POSTGRESQL_CONFIG.get('database')

POSTGRESQL_URI = (
    f'postgresql+psycopg2://{p_user}:{p_password}'
    f'@{p_host}:{p_port}/{p_database}'
)
