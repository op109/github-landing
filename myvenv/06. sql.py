import sqlite3

conn = sqlite3.connect('myvenv/python95.db')

cur  = conn.cursor()

CREATE_SQL = """
    CREATE TABLE IF NOT EXISTS idtem (
        id integer primary key autoincrement,
        code text not null,
        name text not null,
        price integer not null 
    )
"""
cur.execute(CREATE_SQL)

conn.close()