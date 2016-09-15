import socket
import time
import os
from threading import Thread
from _thread import*
import threading
global ip
global port
global s

def socket():
    import socket
    ip=''
    port=18032
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind((ip,port))
    s.listen(5)
    s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    return s

s = socket()
    
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
        print(c, len(c))
        for f in c:
            f.send(message)


def t(conn):
    #print("A")
    #(conn,(ip,port))=s.accept()
    t=ClientThread(ip,port,conn)
    print('a')
    c.append(conn)
    print(len(c))
    #t.start()
    #t.run()
    t.send()




while 1:
    try:
        print('wait')
        s.listen(4)
        #print(len(c))
        print('waiting')
        (conn,(ip,port))=s.accept()
        print(ip, port)
        t1=threading.Thread(target=t, args=(conn,))
        t1.start()
        #t1.run()
        #print('broadcast or chat?')
        #bc = input()
        #print(len(c))
        threads.append(t1)
    except:
        #print("error")
        for connection in c:
            connection.close()
        s.close()
    
for i in threads:
    i.join()

    
