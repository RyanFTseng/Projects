from tkinter import*

master=Tk()


l1=Label(master,text='Ryan').grid(row=0)
b1=Button(master,text="Close",command=master.quit).grid(row=1,column=0)

mainloop()
