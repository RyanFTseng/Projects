import socket

class server:
    def _init_(self):
        
        
       self.socket.socket(socket.AF_INET, socket.SOCK_STREAM)
       self.bind(('127.0.0.1',10502))
       self.listen(1)
       self.conn, self.addr=s.accept()
       print(self.conn)
       self.conn.sendall(data)
       a=self.data.decode()
       if len(a)>0:
            print(a)
       self.conn.recv(1024)
    #def listen1(self):
      #  self.listen(1)
    #def accept(self):
           # conn, addr=self.accept()
            #print('connected by', addr)
            
'''   def senddata(self):
        self.conn.sendall(data)
        a=self.data.decode()
        if len(a)>0:
            print(a)
    def receivedata(self):
            data= self.conn.recv(1024)'''
p=server()

while True:
    p.conn.recv(1024)
    p.receivedata()

