import socket
host='127.0.0.1'
print(host)
port=12345
s=socket.socket(socket.AF_INET, socket. SOCK_STREAM)
s.connect((host,port))
s.sendall(b'Hello,world')
data=s.recv(1024)
s.close()
print('recieved',repr(data))
      
