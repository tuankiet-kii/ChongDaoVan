from tkinter import *

def hello():
    frame2.tkraise()
    print('hello')

def world():
    frame3.tkraise()
    print('world')

root=Tk()

frame1=Frame(root)
frame2=Frame(root)
frame3=Frame(root)

frame1.grid(row=0,column=0,rowspan=2)
frame2.grid(row=0,column=1,rowspan=2)

tag1=Label(frame2,text='hello')
tag2=Label(frame3,text='world')

tag1.grid()
tag2.grid()

press1=Button(frame1,text='hello',command=hello)
press2=Button(frame1,text='world',command=world)

press1.grid(row=0)
press2.grid(row=1)

root.mainloop()