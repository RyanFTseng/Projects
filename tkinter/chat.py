from tkinter import*
import socket


master=Tk()

def enter():
    l=Label(master,text=e1.get()).grid(row=1)


e1=Entry(master)
e1.grid(row=3,columnspan=5)
l1=Label(master,text='').grid(row=1)
b1=Button(master,text='enter',command=enter).grid(row=2,column=0)

while True:
    master.update()
