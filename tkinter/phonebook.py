from tkinter import*
master=Tk()

d={}
d['n']='p'
d.pop('n')
print(d)

def add():
    d[e1.get()]=e2.get()
    print(d)
    e1.delete(0,END)
    e2.delete(0,END)
    l3=Label(master,text=d).grid(row=3,column=0)






e1=Entry(master)
e2=Entry(master)
e1.grid(row=1,column=1)
e2.grid(row=2,column=1)
l1=Label(master,text='name').grid(row=1,column=0)
l2=Label(master,text='number').grid(row=2,column=0)
b1=Button(master,text='add',command=add).grid(row=2,column=2)







    
while True:
    master.update()
