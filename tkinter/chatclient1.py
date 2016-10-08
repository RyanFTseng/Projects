import socket
from threading import Thread
from time import sleep,gmtime,strftime
import time

ip='localhost'
port=1345

def C(s):
    while True:
        print('b')
        #message=input('Client1: Enter message/Enter Exit:')
        #message=message.encode()
        #s.send(message)
        data=s.recv(1024)
        if data!=b'':
            print('client 2 recieved data', data)


try:
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((ip,port))
    print('a')
    t1=threading.Thread(target=C)
    print('b')
    t1.start()
    print('c')
    

except:
    print('error')
    s.close()
