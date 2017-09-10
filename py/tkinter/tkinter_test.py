from tkinter import*

master=Tk()

def print_text():
    print("Name:%s"%e1.get())

l1=Label(master,text='Ryan').grid(row=0)
b1=Button(master,text="Close",command=master.quit).grid(row=1,column=0)
e1=Entry(master)
e1.grid(row=0,column=1)


mainloop()
