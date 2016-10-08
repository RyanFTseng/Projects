import threading
import socket
from time import sleep,gmtime,strftime
from tkinter import*
import threading
import time
master=Tk()
ip='localhost'
port=1234
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((ip,port))
global message
msg=''
message=''
def C():
    global msg
    global message
    message=e1.get()
    s.send(message.encode())
    msg=s.recv(10000)
    print('other clients recieved data', msg)
    


l1=Label(master,text='Client1:').grid(row=0)
l2=Label(master,text=msg).grid(row=1)
e1=Entry(master)
e1.grid(row=2,column=1)
b1=Button(master,text='enter',command=C).grid(row=2,column=0)
b2=Button(master,text='close',command=master.quit).grid(row=3,column=2)

while 1:
    '''global message
    #message=input('Client1 Enter message/ Enter exit:')
    message=message.encode()
    C()'''
    master.update()
    #t1.join(message)

s.close()


