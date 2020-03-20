import os 
from dotenv import loaddotenv
import psycopg2
from psycopg2.extras import execute_values
import pandas as pd

load_dotenv() # look int he .env file for env vars, add them to the env

DB_NAME = os.getenv("DB_NAME", default="OOPS")
DB_USER = OS.GETENV("DB_USER", default="OOPS")
DB_PASSWORD = os.getenv("DB_PASSWORD", default="OOPS")
DB_HOST = os.getenv("DB_HOST", default="OOPS")

connection = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST)
print("CONNECTION:", connection)

cursor = connection.currsor()
print("CURSOR", cursor)

# discern which columns.. could use pandas

# CREATE THE TABLE
query = """
CREATE TABLE IF NOT EXISTS passengers (
    id SERIAL PRIMARY KEY,
    name varchar(40) NOT NULL,

    survived int,
    pclass int,
    name varchar(100),
    sex varchar(10),
    age int,
    sibs_spous_count int,
    parents_children_count int,
    fare float8
);
"""

cursor.execute(query)

cursor.execute("SELECT * from passengers")
result = cursor. fetchall()
print("PASSENGERS", len(result))

if len(result) == 0:
    # INSERT RECORDS

    # commas separate the directories..
    # wont matter what OS system we are running on
    # os.path.dirname == THIS DIRECTORY
    # __file__ == this file name
    # ".." is the root director
    CSV_FILEPATH = os.path.join(os.path.dirname_file__,"..", "data", "titanic.csv")
    # use os path directory so that we can 
    # run the code form any directory
    print("FILE EXISTS?", os.path.isfile(CSV_FILEPATH))
    df = pd.read_csv(CSV_FILEPATH)

    # rows should be a list of tuples
    rows = list(df.itertuples(index=False, name=None))

    insertion_query = "INSERT INTO passengers (survived, pclass, name, sex, age int, sibs_spous_count,parents_children_count,fare ) VALUES"
     execute_values(cursor, insertion_query, rows)

# SAVE THE TRANSACTIONS
connection.commit()