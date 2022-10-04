from sqlalchemy import create_engine
from sqlalchemy.sql import text

eng = create_engine("postgresql://pguser:pgpass@localhost:5401/postgres")
con = eng.connect()
con.execute(text("CREATE TABLE IF NOT EXISTS main_table (text TEXT)"))


def insert_into_main_table(value):
    con.execute(text("INSERT INTO main_table(text) VALUES(\'{}\')".format(value)))
