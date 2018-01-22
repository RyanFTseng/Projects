from tkinter import *
import sqlite3
root=Tk()
root.title("simple exercise using pack")
root.geometry(('600x400'))
conn=sqlite3.connect('phonebook.db')
c=conn.cursor()

first_name = StringVar()
last_name = StringVar()
email=StringVar()
phone_number=StringVar()

def insert():
    first_name = f_name.get()
    last_name = l_name.get()
    email = email.get()
    phone_number = phonenumber.get()
    c.execute('insert into phone_book(first_name,last_name,email,phone_number),values(?,?,?,?)',(first_name, last_name, email, phone_number))
    conn.commit()

def read_from_db():
    listbox=Listbox(root,width=40)
    listbox.grid(row=7,column=1,sticky=W)
    c.execute('select * from phone_book')
    for row in c.fetchall():
        listbox.insert(END,row)

def del_record():
    first = f_name.get()
    c.execute('delete from phone_book where first_name =?',(first,))
    conn.commit()
    listbox=Listbox(root)
    listbox.grid(row=7,column=2)
    c.execute('select * From phone_book')
    for row in c.fetchall():
        listbox.insert(END,row)

def update_record():
    first=f_name.get()
    last=l_name.get()
    email=email.get()
    phone_number=phonenumber.get()
    c.execute('update phone_book set first_name=?, last_name=?, email = ?, phonenumber=? where first_name =?',(first,last,email,phone_number,first,))
    conn.commit()

def clear():
    f_name.delete(0,END)
    l_name.delete(0,END)
    email_address.delete(0,END)
    phonenumber.delete(0,END)


f_name_label = Label(root,text="First name")
f_name_label.grid(row=1,column=1)
f_name=Entry(root)
f_name.grid(row=1,column=2)

l_name_label = Label(root,text="Last name")
l_name_label.grid(row=2,column=1)
l_name=Entry(root)
l_name.grid(row=2,column=2)

email_label = Label(root,text="Email")
email_label.grid(row=3,column=1)
email=Entry(root)
email.grid(row=3,column=2)

phonenumber_label = Label(root,text="Phone Number")
phonenumber_label.grid(row=4,column=1)
phonenumber=Entry(root)
phonenumber.grid(row=4,column=2)

insert= Button(root,text="insert",command=insert)
insert.grid(row=5, column = 2)

root.mainloop()

