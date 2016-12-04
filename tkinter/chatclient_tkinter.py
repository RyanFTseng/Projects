from threading import Thread
import threading
import queue
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
global e1
global window
recvtxt=''
def socket():
        global ip
        global port
        import socket
        ip='localhost'
        port=3955
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((ip,port))
        return s
global s
s=socket()


def addtowindow(recvtxt,window):
        global ip
        global port
        #window.clear()
        window.write(ip+' '+str(port)+':'+recvtxt+' '+'\n')

def send(message):
        if type(message) == str:
                message=message.encode()
                s.send(message)
            
        

def writewindow():
    global e1
    global window
    m=e1.get()
    send(m)
    

def receive(window):
    global recvtxt
    while 1:
        print('b')
        recvtxt=s.recv(1024)
        if recvtxt!=b'':
            recvtxt=recvtxt.decode()
            print('recieved message:'+recvtxt)
            addtowindow(recvtxt,window)
            #l['text']=recvtxt
            #chat.t1.set(recvtxt)


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
            

window = q(master)
e1=Entry(master)
e1.pack()
b1=Button(master,text='send',command=writewindow).pack()
window.pack()
t1=threading.Thread(target=receive, args=(window,))
t1.start()
master.mainloop()
