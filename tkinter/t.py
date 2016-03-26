from tkinter import*
import time

master=Tk()
x=0

def t():
    x=e1.get()
    e1.delete(0,END)
    l2=Label(master,text=x).grid(row=1)
    while int(x)>0:
        time.sleep(1)
        x=int(x)-1
        l2=Label(master,text=int(x)).grid(row=1)
        master.update()
        
def r():
    x=x-x
    l2=Label(master,text=x).grid(row=1)
    master.update()
    
    
l1=Label(master,text='time').grid(row=0)
l2=Label(master,text=x).grid(row=1)
e1=Entry(master)
e1.grid(row=0,column=1)
b1=Button(master,text='close',command=master.quit).grid(row=2,column=2)
b2=Button(master,text='enter',command=t).grid(row=2,column=0)
b3=Button(master,text='reset',command=r).grid(row=2,column=1)

while True:
    master.update()
