import sqlite3
conn=sqlite3.connect('database.db')

c=conn.cursor()
c.execute('CREATE TABLE Categories (CategoryID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,CategoryName NVARCHAR(255),Description NVARCHAR(255))')
c.execute('CREATE TABLE Customers (CustomerID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,CustomerName NVARCHAR(255),ContactName NVARCHAR(255),Address NVARCHAR(255),City NVARCHAR(255),PostalCode NVARCHAR(255),Country NVARCHAR(255))')
c.execute('CREATE TABLE Employees (EmployeeID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,LastName NVARCHAR(255),FirstName NVARCHAR(255),BirthDate DATE,Photo NVARCHAR(255),Notes MEMO)')
c.execute('CREATE TABLE OrderDetails (OrderDetailID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,OrderID INT,ProductID INT,Quantity INT)')                                   
c.execute('CREATE TABLE Orders (OrderID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,CustomerID INT,EmployeeID INT,OrderDate DATE,ShipperID INT)')
c.execute('CREATE TABLE Products (ProductID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,ProductName NVARCHAR(255),SupplierID INT,CategoryID INT,Unit NVARCHAR(255),Price MONEY)')
c.execute('CREATE TABLE Shippers (ShipperID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,ShipperName NVARCHAR(255),Phone NVARCHAR(255))')
c.execute('CREATE TABLE Suppliers (SupplierID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,SupplierName NVARCHAR(255),ContactName NVARCHAR(255),Address NVARCHAR(255),City NVARCHAR(255),PostalCode NVARCHAR(255),Country NVARCHAR(255),Phone NVARCHAR(255))')
      
conn.commit()
c.close()
print('database created successfully')
