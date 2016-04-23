from tkinter import*
master=Tk()
x=0
def  one():
    e1.insert(END,1)
def two():
    e1.insert(END,2)
def three():
    e1.insert(END,3)
def four():
    e1.insert(END,4)
def five():
    e1.insert(END,5)
def six():
    e1.insert(END,6)
def seven():
    e1.insert(END,7)
def eight():
    e1.insert(END,8)
def nine():
    e1.insert(END,9)
def zero():
    e1.insert(END,0)
def plus():
    e1.insert(END,'+')
def sub():
    e1.insert(END,'-')
def mult():
    e1.insert(END,'*')
def divd():
    e1.insert(END,'/')
def eq():
    e1.insert(END,'=')
    x=e1.get()
    l=list(x)
    var=''
    total=0
    operate=0
    ltotal=[]
    ltotal.append(0)
    for i in l:
        if i in ['+','-','*','/','=']:
            ltotal.append(var)
            var=''
            ltotal.append(i)
        else:
            var=var+i
    total=0
    operation='+'
    if ltotal[1]=='':
        ltotal.pop(1)
    for i in ltotal:
        if i in ['+','-','*','/','=']:
            operation=i
        else:
            if operation=='+':
                  total=total+int(i)
            if operation=='-':
                  total=total-int(i)
            if operation=='*':
                  total=total*int(i)
            if operation=='/':
                  total=total/int(i)
            if operation=='=':
                  total=int(i)
    e1.delete(0,END)
    e1.insert(END,total)

def c():
    e1.delete(0,END)
    
e1=Entry(master)
e1.grid(row=0,columnspan=5)
b1=Button(master,text='1',command=one).grid(row=4,column=1)
b2=Button(master,text='2',command=two).grid(row=4,column=2)
b3=Button(master,text='3',command=three).grid(row=4,column=3)
b4=Button(master,text='4',command=four).grid(row=3,column=1)
b5=Button(master,text='5',command=five).grid(row=3,column=2)
b6=Button(master,text='6',command=six).grid(row=3,column=3)
b7=Button(master,text='7',command=seven).grid(row=2,column=1)
b8=Button(master,text='8',command=eight).grid(row=2,column=2)
b9=Button(master,text='9',command=nine).grid(row=2,column=3)
b9=Button(master,text='0',command=zero).grid(row=5,column=3)
bp=Button(master,text='+',command=plus).grid(row=2,column=4)
bs=Button(master,text='-',command=sub).grid(row=3,column=4)
bm=Button(master,text='*',command=mult).grid(row=4,column=4)
bd=Button(master,text='/',command=divd).grid(row=5,column=4)
be=Button(master,text='=',command=eq).grid(row=5,column=2)
bc=Button(master,text='C',command=c).grid(row=5,column=1)

while True:
    master.update()
    
