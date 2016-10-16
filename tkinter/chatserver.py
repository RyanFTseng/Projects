import threading
from threading import Thread
import os
global ip
global port
global s
global f
c=[]
threads=[]
def socket():
   # try:
    import socket
    global f
    ip='localhost'
    port=9993
    filename='ip.txt'
    mode='w'
    f=Filefunction(filename,mode)
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind((ip,port))
    s.listen(5)
    s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    return s
    '''except:
        print('a')
        for connection in c:
            connection.close()
        s.close()'''
    
class Filefunction():
    def __init__(self,filename,mode):
        self.filename=filename
        self.mode=mode
        self.iplist=[]
    def writefile(self,a):
        with open(self.filename,'w') as file:
            file.write(a)
    def readfile(self):
        with open(self.filename,'r') as file:
            for line in file:
                self.iplist.append(line)
        return self.iplist
    def appendfile(self,x):     
        with open(self.filename,'a') as file:
                  file.write(x)
    
class ClientThread(Thread):
    def __init__(self,ip,port,conn):
        global f
        Thread.__init__(self)
        self.ip=ip
        self.port=port
        self.conn=conn
        self.recvport=0
        self.sendport=0
        f.writefile(ip+':'+str(port))
        print('[+] New server socket thread started for'+ip+':'+str(port))
    def run(self):
        while 1:
            data=conn.recv(10000)
            print('server recieved data:', data)
            print('Multithreaded Python server: Waiting for connections from TCP listens...')
            for a in c:
                a.send(data)
                time.sleep(0.01)
    def sendip(self):
        while 1:
            if self.sendport==0:
                i=f.readfile()
                k=','.join(i)
                if k!='':
                    k=k.encode()
                    for a in c:
                        a.send(k)
                self.sendport=1
            else:
                for a in c:
                    message=a.recv(1024)
                    if message!=b'':
                        message=message.decode()
                        print('server received message:'+message)
    def receive(self):
        print('adsde')
        while 1:
            for a in c:
                if self.recvport==0:
                    recvport=a.recv(1024)
                    if recvport!=b'':
                        recvport=recvport.decode()
                        print('server received port:'+recvport)
                        self.recvport=1
                else:
                    message=a.recv(1024)
                    if message!=b'':
                        message=message.decode()
                        print('server received message:'+message)
        
s=socket()
global t
t=None
def create_thread(conn,c):
    global t
    t=ClientThread(ip,port,conn)
    c.append(conn)
    t.sendip()
def create_receive_thread(conn,c):
    global t
    print(t)
    if t!=None:
        t.receive()
    
while 1:
    (conn,(ip,port))=s.accept()
    t1=threading.Thread(target=create_thread, args=(conn,c))
    rt1=threading.Thread(target=create_receive_thread, args=(conn,c))
    t1.start()
    rt1.start()
    threads.append(t1)


