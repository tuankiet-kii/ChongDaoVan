from tkinter import *
import time
from PIL import ImageTk, Image
from tkinter.messagebox import askyesno

app = Tk()
app.geometry("1400x750+250+30")

def change_frame():
    btn1.place_forget()
    fm2.place_forget()
    fm1.place(width=1400, height=700)
def change_frame2():
    btn2.place_forget()
    fm1.place_forget()
    fm2.place(width=1400, height=700)
    btn2.place(x=600,y=550)
btn1 = Button(app,text="Frame1",command=change_frame)
btn1.place(x=400,y=550)
btn2 = Button(app,text="Frame2",command=change_frame2)
btn2.pack()
btn2.place(x=600,y=550)

fm1 = Frame(app)
fm1.pack()
fm1.place(width=1000, height=500)

fm2 = Frame(app)
fm2.pack()
# tạo slider
class slider:
    def __init__(self,root):
        self.root = root
        self.image1 = ImageTk.PhotoImage(Image.open("./img/h1-600-400.jpg"))
        self.image2 = ImageTk.PhotoImage(Image.open("./img/h2-600-400.jpg"))
        Fram_slider =Frame(self.root)
        Fram_slider.place(x=150,y=50,width=600,height=400)
        self.label1 = Label(Fram_slider,image= self.image1,bd=0)
        self.label1.place(x=0,y=0)
        self.label2 = Label(Fram_slider, image=self.image2, bd=0)
        self.label2.place(x=600, y=0)
        self.x = 600
        self.slider_func()
    def slider_func(self):
        self.x-=2/3
        if self.x<=0:
            self.x=1100
            time.sleep(2/3)
            self.new_im = self.image1
            self.image1 = self.image2
            self.image2 = self.new_im
            self.label1.config(image=self.image2)
            self.label2.config(image=self.image1)
        self.label2.place(x=self.x,y=0)
        self.label2.after(1,self.slider_func)

obj = slider(fm1)
app.mainloop()