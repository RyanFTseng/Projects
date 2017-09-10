from threading import Thread
import threading
from time import sleep,gmtime,strftime
import time
from tkinter import filedialog
x=0
from tkinter import*
master=Tk()

                                                                                                        
def socket():
        import socket
        ip='localhost'
        port=3972
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((ip,port))
        return s
s=socket()
def send():
        master.filename=filedialog.askopenfilename(initialdir='/home/pi/ywryantseng',title='select file')
        print(master.filename)
        f=open(master.filename,'r')
        r=f.read(1024)
        message=r
        message=message.encode()
        s.send(message)
def receive():
        while 1:
                message=s.recv(1024)
                if message!=b'':
                        message=message.decode()
                        print('recieved message:'+message)
#t1=threading.Thread(target=send)
#t2=threading.Thread(target=receive)
#t1.start()
#time.sleep(2)
#t2.start()

b1=Button(master,text='send',command=send).pack()
master.mainloop()
