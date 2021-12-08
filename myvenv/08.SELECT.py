import sqlite3

conn = sqlite3.connect('myvenv/python95.db')

cur  = conn.cursor()

SELECT_SQL = "SELECT * FROM item"


cur.execute(SELECT_SQL)

rows = cur.fetchall()
for row in rows:
    print(row)


conn.close()