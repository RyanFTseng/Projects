from threading import Thread
import threading
from time import sleep,gmtime,strftime
import time



def socket():
        import socket
        ip='localhost'
        port=9995
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((ip,port))
        return s
    
s=socket()

def C():
    while True:
        print('d')
        data=s.recv(1024)
        if data!=b'':
            print('client 1 recieved data', data)
        message=input('Client1: Enter message:')
        message=message.encode()
        s.send(message)            
#try:
print('a')
t1=threading.Thread(target=C)
print('b')
t1.start()
print('c')
    

#except:
  #  print('error')
    #s.close()
