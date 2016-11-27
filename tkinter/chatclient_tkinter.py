from threading import Thread
import threading
import Queue
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
        port=8370
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
def receive(chat):
    global recvtxt
    while 1:
        print('b')
        recvtxt=s.recv(1024)
        if recvtxt!=b'':
            recvtxt=recvtxt.decode()
            print('recieved message:'+recvtxt)
            #l['text']=recvtxt
            chat.t1.set(recvtxt)

class q(Text):
        def __init__(self,**options):
                Text.__init__(self,master,**options)
                self.queue=Queue.Queue()
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
                                except Queue.Empty:
                                        pass
                                self.after(100, self.update_me)
        
class chatwindow():
        def __init__(self,master,s):
                self.master=master
                self.e1=Entry(self.master)
                self.e1.pack()
                print('a')
                #self.b1=Button(self.master,text='send',command=txt).grid(row=1,column=2)
                self.t1=  StringVar()
                #Label(self.master,text=self.t1.get()).pack()
                self.t1.set("Hello")
                #self.ihandler()
                master.mainloop()
                #self.master.createfilehandler(s, READABLE, self.ihandler)
        def ihandler(self):
                print("ihandler")
                #t2=threading.Thread(target=receive,args=(,))
                #t2.start()
                #a=1

def Label(chat):               
                print('label')
                Label(chat.master,text=chat.t1.get()).pack()
                chat.master.mainloop()
                
chat=chatwindow(master,s)
t3=threading.Thread(target=Label,args=(chat,))
t3.start()
time.sleep(2)
t2=threading.Thread(target=receive,args=(chat,))
t2.start()

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




#while True:
#        master.mainloop()
