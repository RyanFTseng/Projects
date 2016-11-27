from threading import Thread
import threading
import queue
from time import sleep,gmtime,strftime
import time
from tkinter import*

def socket():
        import socket
        ip='localhost'
        port=8370
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((ip,port))
        return s
global s
s=socket()



def addtowindow(recvtxt,window):
    window.clear()
    while 1:
        window.write(recvtxt)

def receive(window):
    global recvtxt
    while 1:
        print('b')
        recvtxt=s.recv(1024)
        if recvtxt!=b'':
                recvtxt=recvtxt.decode()
        #recvtxt='hello'
                print('recieved message:'+recvtxt)
                addtowindow(recvtxt,window)

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
