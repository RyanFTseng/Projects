import sqlite3
conn = sqlite3.connect('database.db')
c=conn.cursor()
c.execute('INSERT INTO Categories (CategoryName,Description) VALUES ("Beverages","Soft drinks, coffees, teas, beers, and ales")');
c.execute('INSERT INTO Categories (CategoryName,Description) VALUES ("Condiments","Sweet and savory sauces, relishes, spreads, and seasonings")');
c.execute('INSERT INTO Categories (CategoryName,Description) VALUES ("Confections","Desserts, candies, and sweet breads")');
c.execute('INSERT INTO Categories (CategoryName,Description) VALUES ("Dairy Products","Cheeses")');
c.execute('INSERT INTO Categories (CategoryName,Description) VALUES ("Grains/Cereals","Breads, crackers, pasta, and cereal")');
c.execute('INSERT INTO Categories (CategoryName,Description) VALUES ("Meat/Poultry","Prepared meats")');
c.execute('INSERT INTO Categories (CategoryName,Description) VALUES ("Produce","Dried fruit and bean curd")');
c.execute('INSERT INTO Categories (CategoryName,Description) VALUES ("Seafood","Seaweed and fish")');

conn.commit()
c.close()
print('insert all records into customer table successfully')
