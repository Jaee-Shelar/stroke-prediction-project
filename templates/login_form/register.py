from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk  #pip install pillow
from tkinter import messagebox


class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1600x700+0+0")

         #==========bg Image=============
        # self.bg=ImageTk.PhotoImage(file=r"C:\Users\Admin\Mrunal patil\stroke\templates\login_form\bg.jpg")

        # bg_lbl=Label(self.root,image=self.bg)
        # bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)

        #===========left Image=============
        self.bg=ImageTk.PhotoImage(file=r"C:\Users\Admin\Mrunal patil\stroke\templates\login_form\regiimg.png")
        left_lbl=Label(self.root,image=self.bg)
        left_lbl.place(x=60,y=100,width=490,height=550)
        
        #==============main frame============
        frame=Frame(self.root,bg="white")
        frame.place(x=550,y=119,width=700,height=500)

        Register_lbl=Label(frame,text="REGISTER HERE",font=("time new roman",20,"bold"),fg="green",bg="")
        Register_lbl.place(x=20,y=20)




if __name__ == "__main__":
    root=Tk()
    app=Register(root)
    root.mainloop()