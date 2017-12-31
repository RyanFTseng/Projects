import sqlite3
conn = sqlite3.connect('database.db')
c=conn.cursor()
c.execute('INSERT INTO Shippers (ShipperID,ShipperName,Phone) VALUES (1,"Speedy Express","(503) 555-9831")'); 
c.execute('INSERT INTO Shippers (ShipperID,ShipperName,Phone) VALUES (2,"United Package","(503) 555-3199")'); 
c.execute('INSERT INTO Shippers (ShipperID,ShipperName,Phone) VALUES (3,"Federal Shipping","(503) 555-9931")'); 

conn.commit()
c.close()
print('insert all records into Shippers table successfully')
