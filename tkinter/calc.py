from tkinter import*
import time
master=Tk()

x=1
def m():
    1

def  one():
    global x
    e1.insert(0,x)


e1=Entry(master)
e1.grid(row=0,column=5)
b1=Button(master,text='1',command=one).grid(row=4,column=1)
b2=Button(master,text='2',command=m).grid(row=4,column=2)
b3=Button(master,text='3',command=m).grid(row=4,column=3)
b4=Button(master,text='4',command=m).grid(row=3,column=1)
b5=Button(master,text='5',command=m).grid(row=3,column=2)
b6=Button(master,text='6',command=m).grid(row=3,column=3)
b7=Button(master,text='7',command=m).grid(row=2,column=1)
b8=Button(master,text='8',command=m).grid(row=2,column=2)
b9=Button(master,text='9',command=m).grid(row=2,column=3)
b9=Button(master,text='0',command=m).grid(row=5,column=2)
bp=Button(master,text='+',command=m).grid(row=2,column=4)
bs=Button(master,text='-',command=m).grid(row=3,column=4)
bm=Button(master,text='x',command=m).grid(row=4,column=4)
bd=Button(master,text='/',command=m).grid(row=5,column=4)
be=Button(master,text='=',command=m).grid(row=6,column=4)




while True:
    master.update()
    
