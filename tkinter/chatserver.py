import socket

class server:
    def _init_(self,ip,port):
        self.s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind(('127.0.0.1',10502))
    def listen(self):
        self.s.listen()
    def accept(self):
        try:
            self.conn, addr=s.accept()
            print('connected by', addr)
        except:
            conn.close()
    def senddata(self):
        try:
            conn.sendall(data)
            a=data.decode()
            if len(a)>0:
                print(a)
        except:
            conn.close()
    def receivedata(self):
        try:
            data= conn.recv(1024)
        except:
            conn.close()
p=server()
p.listen()
p.accept()
while True:
    p.senddata()
    p.receivedata()
