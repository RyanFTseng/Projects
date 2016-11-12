from threading import Thread
import threading
from time import sleep,gmtime,strftime
import time
x=0

def socket():
        import socket
        ip='localhost'
        port=8346
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((ip,port))
        return s
s=socket()
def send():
        while 1:
                #message=input('Client2: Enter message:')
                #message = "hi client 2"
                message = "Hi"
                message=message.encode()
                s.send(message)
def receive():
        while 1:
                print('receive')
                message=s.recv(1024)
                if message!=b'':
                        message=message.decode()
                        print('recieved message:'+message)

t1=threading.Thread(target=send)
t2=threading.Thread(target=receive)
t2.start()
time.sleep(2)
t1.start()
