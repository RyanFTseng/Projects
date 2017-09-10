from threading import Thread
import threading
import queue
from time import sleep,gmtime,strftime
import time
from tkinter import*


def socket():
        import socket
        global ip
        global port
        ip='localhost'
        port=8373
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((ip,port))
        print('connected to server'+ip+str(port))
        return s
global s
s=socket()

def C():
    while True:
        data=s.recv(1024)
        if data!=b'':
            print('client recieved data', data)


def addtowindow(recvtxt,window):
        #window.clear()
        window.write(ip+str(port)+':'+recvtxt+' ')

def receive(window):
    global recvtxt
    while 1:
        recvtxt=s.recv(1024)
        if recvtxt!=b'':
                recvtxt=recvtxt.decode()
                print('recieved message:'+recvtxt)
                addtowindow(recvtxt,window)
                recvtxt=''

class q(Text):
        def __init__(self,master,**options):
                Text.__init__(self,master,**options)
                self.queue=queue.Queue()
                self.update_me()
        def write(self,line):
                self.queue.put(line)
        def clear(self):
                self.queue.put(None)
        def update_me(self):
            try:
                    while 1:
                            line=self.queue.get_nowait()
                            if line is None:
                                    self.delete(1.0,END)
                            else:
                                    self.insert(END, str(line))
                            self.see(END)
                            self.update_idletasks()
            except queue.Empty:
                pass
            self.after(100, self.update_me)
            
master=Tk()
window = q(master)
e1=Entry(master)
e1.pack()
b1=Button(master,text='send',command=addtowindow).pack()
window.pack()
t1=threading.Thread(target=receive, args=(window,))
t1.start()
master.mainloop()
