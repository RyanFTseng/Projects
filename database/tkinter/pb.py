import sqlite3

conn = sqlite3.connect('phonebook.db')

c = conn.cursor()
c.execute('drop table if exists phone_book')
c.execute('create table phone_book(first_name varchar(20),last_name varchar(20), email varchar(30), phonenumber varchar(10))')
conn.commit()
c.close()
print('phonebook.db created')
       
        
