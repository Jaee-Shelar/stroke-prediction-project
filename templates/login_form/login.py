from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk  #pip install pillow
from tkinter import messagebox

class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1450x800+200+0")

        self.bg=ImageTk.PhotoImage(file=r"C:\Users\Admin\Mrunal patil\stroke\templates\login_form\bgimages2.jpg")

        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        frame=Frame(self.root,bg="black")
        frame.place(x=810,y=125,width=340,height=458)

        img1=Image.open(r"C:\Users\Admin\Mrunal patil\stroke\templates\login_form\logim.jpg")
        img1=img1.resize((100,100),Image.ANTIALIAS)
        self.photoiage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoiage1,bg="black",borderwidth=0)
        lblimg1.place(x=930,y=125,width=100,height=100)

        get_str=Label(frame,text="Get Started",font=("times new romen",18,"bold"),fg="white",bg="black")
        get_str.place(x=95,y=100)

        #label
        username=lbl=Label(frame,text="Username",font=("times new roman",12,"bold"),fg="white",bg="black")
        username.place(x=70,y=150)

        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=180,width=270)

        password=lbl=Label(frame,text="Password",font=("times new roman",12,"bold"),fg="white",bg="black")
        password.place(x=70,y=225)

        self.txtpass=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtpass.place(x=40,y=250,width=270)

        #Icon Images#
        img2=Image.open(r"C:\Users\Admin\Mrunal patil\stroke\templates\login_form\usern.jpg")
        img2=img2.resize((25,25),Image.ANTIALIAS)
        self.photoiage2=ImageTk.PhotoImage(img2)
        lblimg1=Label(image=self.photoiage2,bg="black",borderwidth=0)
        lblimg1.place(x=855,y=275,width=25,height=25)

        img3=Image.open(r"C:\Users\Admin\Mrunal patil\stroke\templates\login_form\passiogo.jpg")
        img3=img3.resize((25,25),Image.ANTIALIAS)
        self.photoiage3=ImageTk.PhotoImage(img3)
        lblimg1=Label(image=self.photoiage3,bg="black",borderwidth=0)
        lblimg1.place(x=855,y=346,width=25,height=25)

        #Loginbutton
        loginbtn=Button(frame,command=self.login,text="Login",font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="black",bg="#ddc0b4",activeforeground="white",activebackground="#ddc0b4")
        loginbtn.place(x=110,y=300,width=120,height=35)

        #registerbutton
        loginbtn=Button(frame,text="New User Register",font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        loginbtn.place(x=0,y=350,width=160)

        #forgetpassbtn
        loginbtn=Button(frame,text="Forget Password",font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        loginbtn.place(x=12,y=370,width=120)
    
    
    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","all field required")
        
        elif self.txtuser.get()=="Mruno" and self.txtpass.get()=="patil":
            messagebox.showinfo("Success","Welcome to Stroke Prediction Website")
        else: 
            messagebox.showerror("Invalid","Invalid UserName$password")



if __name__ == "__main__":
    root=Tk()
    app=Login_Window(root)
    root.mainloop()