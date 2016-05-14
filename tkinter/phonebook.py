from tkinter import*
master=Tk()
d={}
def add():
    d[e1.get()]=e2.get()
    print(d)
    f=open('pb.txt','a')
    f.write(e1.get())
    f.write(':')
    f.write(e2.get())
    f.write('\n')
    f.close()
    '''for i in f:
        print(i)
        print(type(i),type(e1.get()))
        print('i=',i,'e1=',e1.get())
        if e1.get() in i:
            print ('hello')
            print (e1.get())
            print('item already exists in file')
        else:
                fl=open('pb.txt','a')
                print('item is not here')
                
    f.close()
    '''
    
    
    e1.delete(0,END)
    e2.delete(0,END)
def remove():
    e2.delete(0,END)
    d.pop(e1.get())
    print(d)
    e1.delete(0,END)
    e2.delete(0,END)
def show():
    e2.delete(0,END)
    x=e1.get()
    f=open('pb.txt','r')
    for  i in f:
        if x in i:
            i=i.strip()
            for j in range(len(i)):
                if i[j]==':':
                    k=j
            print(i[k+1:])
                    
            print(i[-1])
    f.close()
    #print(d.get(x))
    #e2.insert(END,d.get(x))

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

