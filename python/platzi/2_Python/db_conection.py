import pandas as pd

import sqlalchemy as sql

from sqlalchemy import create_engine

import pymysql

pymysql.install_as_MySQLdb()

database_type = 'mysql'

user = 'root'
password = ''
host = 'localhost'
database = 'cartech'

conn_string = '{}://{}:{}@{}/{}'.format(database_type, user, password, host, database)

sql_conn = sql.create_engine(conn_string)

query_sql = '''select * from equipo limit 10'''

df = pd.read_sql(query_sql, sql_conn)


print (df)