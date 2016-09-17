# -*- coding: utf-8 -*-
import socket
import threading
from time import sleep,gmtime,strftime
from tkinter import*
import time
master=Tk()

    

ip='localhost'
port=18039

 
def C():
    while True:
    #s.send(message)
        #time.sleep(0.01)
        data=s.recv(1024)
        if data!=b'':
            print('client 2 recieved data', data)

    
#message=input('Client1: Enter message/Enter Exit:')
#message=message.encode()
try:
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((ip,port))
    t1=threading.Thread(target=C)
    t1.start()

except:
    print('error')
    s.close()
