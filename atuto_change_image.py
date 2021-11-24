from tkinter import *
from PIL import  ImageTk,Image

app = Tk()
app.geometry("1400x750+300+100")
hinh1 = ImageTk.PhotoImage(Image.open("./img/images.png"))
hinh2 = ImageTk.PhotoImage(Image.open("./img/truong-hutech.jpg"))
hinh3 = ImageTk.PhotoImage(Image.open("./img/hutech.jpg"))
hinh4 = ImageTk.PhotoImage(Image.open("./img/img2.png"))
label1 = Label(app,image= hinh1,bd=0)
label1.pack()
label1.place(x=0,y=0)
x=1
def move():
    global x
    if x==4:
        x=1
    if x==1:
        label1.config(image=hinh1)
    elif x==2:
        label1.config(image=hinh2)
    elif x==3:
        label1.config(image=hinh3)
    elif x==4:
        label1.config(image=hinh4)
    x+=1
    label1.after(2000,move)
move()

app.mainloop()