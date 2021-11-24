from tkinter import *
from PIL import ImageTk, Image
from tkinter.messagebox import askyesno
import time



# root = Tk()
# root.geometry("1000x600+400+150")
# img = ImageTk.PhotoImage(Image.open("./img/superman.jpg"))
# panel = Label(root, image=img)
# panel.pack(side="bottom", fill="both", expand="yes")
# root.mainloop()

class slider:
    def __init__(self,root):
        self.root = root
        self.root.title("slider")
        self.root.geometry("900x700+500+100")
        # self.img = ImageTk.PhotoImage(Image.open("./img/quoc_ky.jpg"))
        # self.panel = Label(self.root, image=self.img)
        # self.panel.pack(side="bottom", fill="both", expand="yes")
        self.image1 = ImageTk.PhotoImage(Image.open("./img/hutech1.jpg"))
        self.image2 = ImageTk.PhotoImage(Image.open("./img/hutech2.jpg"))
        Fram_slider =Frame(self.root)
        Fram_slider.place(x=150,y=50,width=600,height=400)
        self.label1 = Label(Fram_slider,image= self.image1,bd=0)
        self.label1.place(x=0,y=0)
        self.label2 = Label(Fram_slider, image=self.image2, bd=0)
        self.label2.place(x=600, y=0)
        self.x = 600
        self.slider_func()
        def confirm():
            answer = askyesno(title='Xác nhận thoát ứng dụng',
                              message='Bạn có chắc muốn thoát ứng dụng?')
            if answer:
                self.root.destroy()
        Label(self.root,text="CHÀO MỪNG BẠN ĐẾN VỚI HỆ THỐNG CHỐNG ĐẠO VĂN",font=("Arial",20,'bold')).place(x=80,y=500)
        Button(self.root,text="ĐĂNG NHẬP VÀO ỨNG DỤNG",width=40,height=2,bg="light green").place(y=570,x=300)
        Button(self.root, text="THOÁT ỨNG DỤNG", width=25,height=2,bg="orange",command=confirm).place(y=630, x=350)
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


fm_main = Tk()
obj = slider(fm_main)
fm_main.mainloop()