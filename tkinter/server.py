import socket
import time
import os
from threading import Thread
from _thread import*

host='127.0.0.1'
port=8755
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((host,port))
s.listen(5)
def serverThread():
    conn,addr=s.accept()
    print('got connection from',addr)
    while 1:
        data=conn.recv(1024)
        
        print('get data',data)
        if not data:
            time.sleep(1)
            break
        conn.sendall(data.upper())
  
for i in range(5):
    t=Thread(target=serverThread)
    t.start()
s.close()
