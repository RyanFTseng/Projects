import threading
from threading import Thread
import os
import time
global ip
global port
global s
global f
c=[]
d={}
threads=[]
p=[]
def socket():
   # try:
    import socket
    global f
    ip='localhost'
    port=3955
    filename='ip.txt'
    mode='w'
    f=Filefunction(filename,mode)
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind((ip,port))
    s.listen(5)
    s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    return s

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
                  
    def checkport(self,message):
        with open(self.filename,'r') as file:
            for line in file:
                e,f=line.split(':')
                if message==f:
                    return True
            return False
        
class ClientThread(Thread):
    def __init__(self,ip,port,conn):
        global f
        Thread.__init__(self)
        self.ip=ip
        self.port=port
        self.conn=conn
        self.recvport=0
        self.sendport=0
        self.dict_port=0
        d[self.port]=0
        self.message=''
        f.writefile('')
        f.appendfile(ip+':'+str(port))
        f.appendfile('\n')
        print('[+] New server socket thread started for'+ip+':'+str(port))
        p.append(self.port)
        
        
    def run(self):
        while 1:
            data=conn.recv(10000)
            print('server recieved data:', data)
            print('Multithreaded Python server: Waiting for connections from TCP listens...')
            for a in c:
                a.send(data)
                time.sleep(0.01)
                
    def sendip(self):
        pass
        '''while 1:
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
                    if self.message!='':
                    #message=input('Server: Enter message:')
                        a.send(self.message)'''
        '''for a in c:
            print('sss')
            #if self.dict_port==0:
            cport=a.recv(1024)
            if cport!=b'':
                cport=cport.decode()
                print('server received message send:'+cport)
                check=f.checkport(cport)
                self.dict_add(cport)
                print(check)
            self.dict_port=1
            else:
                message=a.recv(1024)
                if message!=b'':
                    message=message.decode()
                    print('server received message send:'+message)  '''                      

    def dict_add(self,cport):
        if self.port!=cport:
                d[self.port]=cport
                
    def receive(self):
        while 1:
            for a in c:
                for b in c:
                    #p1=b.getpeername()
                    #print(p1[1],b)
                            #if q==p1[1]:
                    #sself.message=self.message.decode()
                    print("Message",self.message)
                    if type(self.message)==str:
                        self.message=self.message.encode()
                        if self.message!=b'':
                            b.send(self.message)
                    else:
                        if self.message!=b'':
                            b.send(self.message)
               
                self.message=a.recv(1024)
                if self.message!=b'':
                    self.message=self.message.decode()
                    print('server received message:'+self.message)
            
        
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
    time.sleep(2)
    rt1.start()
    threads.append(t1)


