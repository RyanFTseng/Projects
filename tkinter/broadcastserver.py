import socket
import time
import os
from threading import Thread
global ip
global port
global s
s = socket()
z = []
threads=[]
c=[]

#socket function
def socket():
    try:
        ip=''
        port=18039
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.bind((ip,port))
        s.listen(5)
        s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        return s
    except:
        for connection in c:
            connection.close()
        s.close()

#create server thread
class ClientThread(Thread):
    def __init__(self,ip,port,conn):
        Thread.__init__(self)
        self.ip=ip
        self.port=port
        self.conn=conn
        print('[+] New server socket thread started for'+ip+':'+str(port))
    #recieve data
    def run(self):
        while 1:
            data=conn.recv(10000)
            print('server recieved data:', data)
            print('Multithreaded Python server: Waiting for connections from TCP listens...')
            for a in c:
                a.send(data)
                time.sleep(0.01)
    #broadcast
    def send(self):
        while 1:
            message=input('Multithreaded Python server:Enter response from Server/Enter exit:')
            message=message.encode()
            for f in c:
                f.send(message)

#create broadcast thread
def create_thread(conn):
    try:
        global z
        t=ClientThread(ip,port,conn)
        c.append(conn)
        t.send()
    except:
        print('error')

while 1:
    try:
        s.listen(4)
        (conn,(ip,port))=s.accept()
        t1=threading.Thread(target=create_thread, args=(conn,))
        t1.start()
        threads.append(t1)
    except:
        for connection in c:
            connection.close()
        s.close()
    
for i in threads:
    i.join()

    
