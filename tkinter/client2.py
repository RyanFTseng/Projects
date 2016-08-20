import socket
from time import sleep,gmtime,strftime
from tkinter import*
master=Tk()

message=input('Client2: Enter message/Enter Exit:')
message=message.encode()
host='0.0.0.0'
port=2004
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host,port))

while message!='exit':
    s.send(message)
    data=s.recv(10000)
    print('recieved data', data)

    message=input('Client1: Enter message/ Enter exit:')
    message=message.encode()
s.close()


'''def enter():
    l1=Label(master,text='                                                                                                                                                                                                                                                                           ').grid(row=1)
    global Input
    Input=e1.get()
    s.send((Input+' '+'from client2:').encode())
    reserver_data=s.recv(1024)
    print('recieved from server:',reserver_data)
    l1=Label(master,text='client2:'+Input).grid(row=1)
    master.update()
    e1.delete(0,END)
    
    
    
    
e1=Entry(master)
e1.grid(row=3,columnspan=5)
b1=Button(master,text='enter',command=enter).grid(row=2,column=0)



while 1:
    localTime=strftime('%H:%M:%S',gmtime())
    s.sendto(("packet_time="+localTime).encode(),(host,port))
    print("sending packet..."+str(localTime))
    Input=input('Input from client2:')
    s.send((Input+'from client2').encode())
    reserver_data=s.recv(1024)
    print('recieved from server:',reserver_data)
s.close

while True:
    master.update()'''
