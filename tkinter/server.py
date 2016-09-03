import socket
import time
import os
from threading import Thread
from _thread import*
import threading

ip='0.0.0.0'
port=18022
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
            print('Multithreaded Python server: Waiting for connections from TCP listens...')
            #print('broadcast or chat?')
            #if input()=='broadcast':
            #    t.send()
            #print(len(c))
            for a in c:
                a.send(data)
                time.sleep(0.01)
            #conn.send(message)
    def send(self):
        message=input('Multithreaded Python server:Enter response from Server/Enter exit:')
        message=message.encode()
        print(c)
        for f in c:
            f.send(message)
def t():
    (conn,(ip,port))=s.accept()
    t=ClientThread('0.0.0.0',2004,conn)
    c.append(conn)
    #t.start()
    #t.run()


s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

while 1:
    try:
        s.listen(4)
        print(len(c))
        t1=threading.Thread(target=t)
        t1.start()
        #t1.run()
        print('broadcast or chat?')
        #bc = input()
        print(len(c))
        threads.append(t)
    except:
        for connection in c:
            connection.close()
    
for i in threads:
    i.join()

s.close()
