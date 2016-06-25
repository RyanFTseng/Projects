import socket
host= '127.0.0.1'
port=10502

class socket:
    def _init_(self,ip,port):
        self.s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind((host,port))
    def listen(self):
        self.s.listen(5)
    def accept(self):
        self.conn, addr=s.accept()
        print('connected by', addr)
    def senddata(self):
        conn.sendall(data)
        a=data.decode()
        if len(a)>0:
            print(a)
    def receivedata(self):
        data= conn.recv(1024)
        
        


try:
    
    while True:
        
        '''if not data: break'''
        conn.sendall(data)
        a=data.decode()
        if len(a)>0:
            print(a)
except:
    conn.close()
