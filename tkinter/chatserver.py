import socket


class socket:
    def _init_(self,ip,port):
        try:
            self.s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.s.bind(('127.0.0.1',10502))
        except:
            conn.close()
    def listen(self):
        try:
            self.s.listen(5)
        except:
            conn.close()
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
        
        



