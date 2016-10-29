from threading import Thread
import threading
from time import sleep,gmtime,strftime
import time
x=0

def socket():
        import socket
        ip='localhost'
        port=8325
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((ip,port))
        return s
    
s=socket()

def C():
        global x
        while True:
                data=s.recv(1024)
                if data!=b'':
                    print('client 1 recieved data:', data)
                if x==0:
                        p=input('Enter port:')
                        p=p.encode()
                        s.send(p)
                        x=1
                else:
                        message=input('Client1: Enter message:')
                        message=message.encode()
                        s.send(message) 
#try:
t1=threading.Thread(target=C)
t1.start()
#except:
  #  print('error')
    #s.close()
