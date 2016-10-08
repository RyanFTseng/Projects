from threading import Thread
import socket
import os
import time
from tkinter import*
master=Tk()

 
ip='localhost'
port=1234
threads=[]
c=[]
ports=[1234,1235]
sockets=[]
t=[]
class ClientThread(Thread):
    def __init__(self,ip,port):
        Thread.__init__(self)
        self.ip=ip
        self.port=port
        self.s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.s.bind((ip,port))
        self.s.listen(4)
        self.conn=self.s.accept()[0]
        self.s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        
        print('[+] New server socket thread started for'+ip+':'+str(port))
        self.run()
    def run(self):
        while 1:
            print('aaaa')
            data=self.conn.recv(10000)
            if data==b'':
                break
            print('server recieved data:', data)
            self.conn.send(data)

#for port in ports:
 #   s.append(socket.socket(socket.AF_INET,socket.SOCK_STREAM))
'''s0=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s1=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s0.bind((ip,1234))
s1.bind((ip,1235))
s1.listen(4)
s0.listen(4)'''

'''print('a')
(conn,(ip,port))=s.accept()
print('b')
c.append(conn)'''
print('Multithreaded Python server: Waiting for connections from TCP listens...')
for port in ports:
    t.append(ClientThread(ip,port))
for n in t:
    n.start()
'''t=ClientThread(ip,port,conn)
t.start()
threads.append(t)'''

'''s0.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s1.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)'''  
for i in t:
    i.join()


    

l1=Label(master,text=data).grid(row=0)


while 1:
    master.update()  
#s.close()
