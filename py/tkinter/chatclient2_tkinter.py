from threading import Thread
import threading
from time import sleep,gmtime,strftime
import time
from tkinter import*
master=Tk()
x=0
txt=0
global message
global recvtxt
recvtxt=''
def socket():
        import socket
        ip='localhost'
        port=8357
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((ip,port))
        return s
s=socket()
def send():
    global txt
    message=txt
    print(txt)
    message=message.encode()
    s.send(message)
def receive():
    global recvtxt
    while 1:
        recvtxt=s.recv(1024)
        if recvtxt!=b'':
            recvtxt=recvtxt.decode()
            print('recieved message:'+recvtxt)

def sendthread():
    t1=threading.Thread(target=send)
    t1.start()
    time.sleep(2)
t2=threading.Thread(target=receive)
t2.start()

def txt():
    global txt
    txt=e1.get()
    print(txt)
    sendthread()


class chatwindow():
        def __init__(self,master,s):
                self.master=master
                self.e1=Entry(self.master)
                e1.grid(row=1,column=1)
                self.b1=Button(self.master,text='send',command=txt).grid(row=1,column=2)
                self.l1=Label(self.master,text='').grid(row=0)
                self.master.createfilehandler(s, READABLE, self.ihandler)
        def ihandler(self):
                self.l1['text']=recieve()
chatwindow()
while True:
        master.update()
