import pandas as pd
import sqlite3

df = pd.read_csv('buddymove_holidayiq.csv')
print('shape:', df.shape)

conn = sqlite3.connect('buddymove_holidayiq.sqlite3')

buddy = df.to_sql('buddymove_holidayiq', conn)

updated_conn = sqlite3.connect(buddy)