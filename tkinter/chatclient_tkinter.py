from threading import Thread
import threading
from time import sleep,gmtime,strftime
import time
from tkinter import*
master=Tk()
x=0
global a
a=0
txt=0
global message
global recvtxt
recvtxt=''
def socket():
        import socket
        ip='localhost'
        port=8367
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((ip,port))
        return s
global s
s=socket()

def send():
    global message
    global txt
    message=txt
    print(txt)
    message=message.encode()
    s.send(message)

    
chat=chatwindow(master,s)


def receive(l):
    global recvtxt
    while 1:
        print('b')
        recvtxt=s.recv(1024)
        if recvtxt!=b'':
            recvtxt=recvtxt.decode()
            print('recieved message:'+recvtxt, type(l))
            #l['text']=recvtxt
        chat.t1=recvtxt
def sendthread():
    t1=threading.Thread(target=send)
    t1.start()
    time.sleep(2)
#t2=threading.Thread(target=receive)
#t2.start()

def txt():
    global txt
    txt=e1.get()
    print(txt)
    sendthread()

class chatwindow():
        def __init__(self,master,s):
                self.master=master
                self.e1=Entry(self.master)
                self.e1.pack()
                print('a')
                #self.b1=Button(self.master,text='send',command=txt).grid(row=1,column=2)
                t1=  StringVar()
                print(t1)
                
                Label(self.master,text=t1.get()).pack()
                t1.set("Hello")
                self.ihandler()
                master.mainloop()
                #self.master.createfilehandler(s, READABLE, self.ihandler)
        def ihandler(self):
                print("ihandler")
                t2=threading.Thread(target=receive,args=("",))
                t2.start()
                a=1
t3=threading.Thread(target=Label,args=(chat))
t3.start()
def Label(chat):               
        if a==1:
                Label(chat.master,text=chat.t1.get()).pack()
                chat.master.mainloop()


        


#while True:
#        master.mainloop()
