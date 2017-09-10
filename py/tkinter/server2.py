import socket
import time
from threading import Thread
from _thread import*

ip='0.0.0.0'
port=2004

class ClientThread(Thread):
    def _init_(self,ip,port):
        Thread._init_(self)
        self.ip=ip
        self.port=port
        print('[+] New server socket thread start for' +ip+':'+str(port))
    def run(self):
        while 1:
            data=conn.recv(10000)
            print('server recieved data:',data)
            message=input('Multithreaded python server : Enter Response from Server/Enter exit:')
            message=message.encode()
            if message=='exit':
                break
            conn.send(message)

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind((ip,port))
threads=[]
while 1:
    s.listen(4)
    print('multithreaded by python server: waiting for connections from TCP listens...')
    (conn,(ip,port))=s.accept()
    #t=Thread(target=ClientThread,args=(ip,port))
    t=ClientThread('0.0.0.0',2004)
    t.start()
    threads.append(t)
for i in threads:
    i.join()

'''def serverThread():
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
s.close()'''
