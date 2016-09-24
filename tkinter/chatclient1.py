import socket
from threading import Thread
from time import sleep,gmtime,strftime
from tkinter import*
import time

ip='localhost'
port=18039
message=input('Client1: Enter message/Enter Exit:')
message=message.encode()



def C():
    while True:
        s.send(message)
        data=s.recv(1024)
        if data!=b'':
            print('client 2 recieved data', data)


try:
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((ip,port))
    t1=threading.Thread(target=C)
    t1.start()

except:
    print('error')
    s.close()
