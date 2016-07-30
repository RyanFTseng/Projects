import socket
from time import sleep,gmtime,strftime

host='127.0.0.1'
port=5602
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host,port))
while 1:
    localTime=strftime('%H:%M:%S',gmtime())
    s.sendto(("packet_time="+localTime).encode(),(host,port))
    print("sending packet..."+str(localTime))
    Input=input('Input from client1:')
    s.send((Input+'from client1').encode())
    reserver_data=s.recv(1024)
    print('recieved from server:',reserver_data)
s.close
