# -*- coding: utf-8 -*-
import socket
import threading
from time import sleep,gmtime,strftime
from tkinter import*
import time
master=Tk()

    

ip='localhost'
port=8370

 
def C():
    while True:
        data=s.recv(1024)
        if data!=b'':
            print('client 2 recieved data', data)


try:
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    print('a')
    s.connect((ip,port))
    print('b')
    t1=threading.Thread(target=C)
    print('c')
    t1.start()

except:
    print('error')
    s.close()
