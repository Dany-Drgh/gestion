import pandas as pd
import sqlite3
# import the path to the database
from utils.paths import path_to_db

def import_csv_to_db(filename, table_name):
    #connect to the database
    conn = sqlite3.connect(path_to_db)
    c = conn.cursor()
    #read the csv file
    df = pd.read_csv(filename)
    #check if the table exists
    c.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}'")
    if c.fetchone() is None:
        print(f"Table {table_name} does not exist")
        return
    #check if the table has the same columns as the csv file
    c.execute(f"PRAGMA table_info('{table_name}')")
    table_columns = [column[1] for column in c.fetchall()]
    if table_columns != list(df.columns):
        print(f"Table {table_name} does not have the same columns as the csv file")
        return
    #insert the data into the database
    for row in df.itertuples(index=False):
        c.execute(f"INSERT INTO {table_name} VALUES ({','.join('?'*len(row))})", row)
    conn.commit()
    print(f"\33[92m\33[1mData imported to {table_name} table\33[0m")
