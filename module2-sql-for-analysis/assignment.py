import psycopg2
import pandas
import csv
import os

print(os.environ)
exit()
# MAKE SURE TO TAKE OUT PASSWORD BEFORE COMMITING

# credentials for elephantSQL
# set what we need to know to connect to the database
dbname = "ljcmelcd"
user = "ljcmelcd"
password = "9BGqkuJs0Av6tVrVdwcCTZoMRmCP4jbF"
host = "drona.db.elephantsql.com"

# get connection object
pg_conn = psycopg2.connect(dbname=dbname, user=user,
password=password, host=host)

# use the connection to get a cursor
pg_curs = pg_conn.cursor()

query = """CREATE TABLE IF NOT EXISTS titanic(
    survived INT,
    pclass INT,
    name VARCHAR(100),
    sex VARCHAR(10),
    age FLOAT,
    siblings_spouses_abd INT,
    parents_children_abd INT,
    fare FLOAT)
"""
try:
    pg_curs.execute(query)
    print("YAY!")
except Exception as ex:
    print(ex)

with open('titanic.csv', 'r') as f:
    next(f)
    pg_curs.copy_from(f, 'titanic', sep=",")
    pg_conn.commit()


# query_2 = """COPY titanic FROM './titanic.csv' WITH (FORMAT csv)"""

# try:
#     pg_curs.execute(query_2)
#     print("DID IT")
# except Exception as ex:
#     print(ex)
