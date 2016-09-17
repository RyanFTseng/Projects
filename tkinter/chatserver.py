import socket
from threading import Thread
from _thread import*
import threading



def socket():
    try:
        import socket
        ip=''
        port=18039
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.bind((ip,port))
        s.listen(5)
        s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        return s
    except:
    for connection in c:
        connection.close()
    s.close()
