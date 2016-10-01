import socket
from threading import Thread
import threading
import os
global ip
global port
global s
global f
c=[]
threads=[]
def socket():
    try:
        import socket
        global f
        ip=''
        port=18039
        filename='ip.txt'
        mode='w'
        f=Filefunction(filename,mode)
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.bind((ip,port))
        s.listen(5)
        s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        return s
    except:
        for connection in c:
            connection.close()
        s.close()

class Filefunction():
    def __init__(self,filename,mode):
        self.filename=filename
        self.f=open(self.filename,mode)
        self.iplist=[]
    def writefile(self,a):
        self.f.write(a)
    def readfile(self):
        for line in f:
               iplist.append(f)
        return iplist
    def appendfile(self,x):     
        self.f.append(x)
        
class ClientThread(Thread):
    def __init__(self,ip,port,conn):
        global f
        Thread.__init__(self)
        self.ip=ip
        self.port=port
        self.conn=conn
        f.writefile(ip)
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
            i=f.readfile()
            for a in c:
                a.send(','.join(i))
s=socket()
def create_thread(conn):
    t=ClientThread(ip, port, conn)
    c.append(conn)
    t.sendip()
    
while 1:
    s.listen(4)
    (conn,(ip,port))=s.accept()
    t1=threading.Thread(target=create_thread, args=(conn,))
    t1.start()
    threads.append(t1)
