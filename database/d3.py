import sqlite3
conn=sqlite3.connect('database.db')
c=conn.cursor()

#c.execute('select count(customerid), country from customers group by country')
#c.execute('select count(customerid), country from customers group by country order by count(customerid) desc')
#c.execute('select count(shipperid), orderid from orders group by shipperid')
#c.execute('select count(customerid), country from customers group by country order by count(customerid) desc limit 5')
#c.execute('select count(employeeid), orderid from orders group by employeeid order by count(employeeid) desc limit 8')
#c.execute('select count(employeeid), employeeid from orders group by employeeid ')
#c.execute('select productname from products where productid = any(selectproductid from orderdetails where quantity=10')
#c.execute('select count(customerid),country from customers group by country having count(customerid)>5')
#c.execute('select count(customerid), country from customers group by country having count(customerid)>5 order by count(customerid) desc')
#c.execute('select count(employeeid), employeeid from orders group by employeeid having count(employeeid)>10')
c.execute('select count(employeeid),from orders inner join employees on orders.employeeid = employees.employeeid employees where lastname = "Davolio" group by employeeid having count(employeeid)>25')







for n in c.fetchall():
    print(n)
conn.commit()
c.close()
