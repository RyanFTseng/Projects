import sqlite3
conn = sqlite3.connect('database.db')
c=conn.cursor()
c.execute('select * from Categories')
for n in c.fetchall():
    print(n)
conn.commit()
c.close()
