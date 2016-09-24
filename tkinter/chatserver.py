import socket
from threading import Thread
import os

def socket():
    try:
        import socket
        ip=''
        port=18039
        filename='ip.txt'
        mode='w'
        f=File(filename,mode)
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.bind((ip,port))
        s.listen(5)
        s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        return s
    except:
        for connection in c:
            connection.close()
        s.close()

class File():
    def __init__(self,filename,mode):
        self.filename=filename
        self.f=open(self.filename,mode)
    
    def writefile(self,a):
        self.f.write(a)
        
    def readfile(self):
        for line in f:
            print(f)
            
    def appendfile(self,x):     
        self.f.append(x)
    
    


        
class ClientThread(Thread):
    def __init__(self,ip,port,conn):
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
                
