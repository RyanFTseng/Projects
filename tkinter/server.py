import socket
import time
import os
from threading import Thread
from _thread import*

ip='0.0.0.0'
port=19991
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((ip,port))
s.listen(5)
threads=[]
c=[]
class ClientThread(Thread):
    def __init__(self,ip,port,conn):
        Thread.__init__(self)
        self.ip=ip
        self.port=port
        self.conn=conn
        print('[+] New server socket thread started for'+ip+':'+str(port))
    def run(self):
        while 1:
            data=conn.recv(10000)
            print('server recieved data:', data)
            #message=input('Multithreaded Python server:Enter response from Server/Enter exit:')
            #message=message.encode()
            #if message=='exit':
            #    break
            print(len(c))
            for a in c:
                a.send(data)
            #conn.send(message)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

while 1:
    s.listen(4)
    print('Multithreaded Python server: Waiting for connections from TCP listens...')
    (conn,(ip,port))=s.accept()
    c.append(conn)
    t=ClientThread('0.0.0.0',2004,conn)
    t.start()
    #t.run()
    threads.append(t)
    
for i in threads:
    i.join()

s.close()
