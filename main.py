import sqlalchemy as db
import pymysql

config = {
	'host': 'localhost',
	'port': 3307,
	'user': 'root',
	'password': 'mysqlpassmacrob',
	'database': 'python_db'
}

db_user = config.get('user')
db_pwd = config.get('password')
db_host = config.get('host')
db_port = config.get('port')
db_name =config.get('database')

connection = f"mysql+pymysql://{db_user}:{db_pwd}@{db_host}:{db_port}/{db_name}"
engine = db.create_engine(connection)
connection_ = engine.connect()

metadata = db.Metadata(bind=engine)
metadata.reflect(only=['python_table'])

python_table = metadata.tables['python_table']

python_table
