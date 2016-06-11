from tkinter import*
master=Tk()
d={}

f=open('pb.txt','r')
for n in f:
    a,b=n.split(':')
    print(a)
    print(b)
    d[a]=b
    print(d)
f.close()

def add():
    d[e1.get()]=e2.get()
    f=open('pb.txt','a')
    f.write(e1.get())
    f.write(':')
    f.write(e2.get())
    f.write('\n')
    f.close()
    e1.delete(0,END)
    e2.delete(0,END)
    print(d)
    
def remove():
    print(d,'printing d')
    print(e1.get(),'e1')
    d.pop(e1.get())
    print(d,'printing d')
    e1.delete(0,END)
    e2.delete(0,END)
    f=open('pb.txt','w')
    for n in d:
        v=n +':'+ d[n]
        f.write(v)
        f.write('\n')
    f.close()
    
def show():
    e2.delete(0,END)
    x=e1.get()
    e2.insert(0,d[x])

        
e1=Entry(master)
e2=Entry(master)
e1.grid(row=1,column=1)
e2.grid(row=2,column=1)
l1=Label(master,text='name').grid(row=1,column=0)
l2=Label(master,text='number').grid(row=2,column=0)
b1=Button(master,text='add',command=add).grid(row=3,column=0)
b2=Button(master,text='remove',command=remove).grid(row=3,column=1)
b3=Button(master,text='show',command=show).grid(row=3,column=2)

while True:
    master.update()

