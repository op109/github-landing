import sqlite3

conn = sqlite3.connect('myvenv/python95.db')

cur  = conn.cursor()

INCERT_SQL = "INSERT INTO item(code, name, price) VALUES (?, ?, ?)"

data = (
    ('A00002', '에어컨 20평형', 350000),
    ('A00003', '최신형 스마트폰', 800000),
    ('A00004', '가성비 노트북', 650000)
)

cur.executemany(INCERT_SQL, data)

conn.commit()

conn.close()