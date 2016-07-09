from tkinter import*
import socket
master=Tk()


class client:
    def _init_(self,ip,port):
        self.s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind(('127.0.0.1',10502))
    def senddata(self):
        self.s.sendall(e1.get().encode())
    def recievedata(self):
        data=s.recv(1024)
        print('recieved',repr(data))
def enter():
    e1.delete(0,END)

e1=Entry(master)
e1.grid(row=3,columnspan=5)
l1=Label(master,text='').grid(row=1)
b1=Button(master,text='enter',command=enter).grid(row=2,column=0)
c=client()

c.senddata()
c.recievedata()


while True:
        master.update()










    
