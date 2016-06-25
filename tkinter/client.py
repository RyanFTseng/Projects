from tkinter import*
import socket
host= '127.0.0.1'
port=10502

master=Tk()

s=socket.socket(socket.AF_INET, socket. SOCK_STREAM)
s.connect((host,port))

def enter():
    l=Label(master,text=e1.get()).grid(row=1)
    #s.sendall(b'hello,world')
    s.sendall(e1.get().encode())
    data=s.recv(1024)
    print('recieved',repr(data))
    e1.delete(0,END)

e1=Entry(master)
e1.grid(row=3,columnspan=5)
l1=Label(master,text='').grid(row=1)
b1=Button(master,text='enter',command=enter).grid(row=2,column=0)

while True:
    master.update()
