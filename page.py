from cProfile import label
from email.mime import image 
from tkinter import *
from tkinter import ttk, messagebox
from tkinter import font
from PIL import Image,ImageTk
import pymysql
class Register:
    def __init__(self,root):
        self.root=root
        self.root.title('login')
        self.root.geometry('1350x700+0+0')
        self.root.configure(bg="white")
        self.root.resizable(True,True)

        self.img= ImageTk.PhotoImage(Image.open('D:\\python programming\\img\\R.JFIF'))
        img=Label(self.root,image=self.img).place(x=0,y=0,relwidth=1,relheight=1)

        frame=Frame(root,width=350,height=350,bg="grey")
        frame.place(x=500,y=180)
        heading=Label(frame,text='SIGN IN',bg="grey", font=("times new roman",25,"bold"))
        heading.place(x=120,y=5)

        tit=Label(text='DISEASE PREDICTION SYSTEM',bg="lightgrey", font=("times new roman",30,"bold"))
        tit.place(x=400,y=5)
        title=Label(text='FOR AN EXISTING USER',bg="lightgrey", font=("times new roman",15,"bold"))
        title.place(x=600,y=80)

 
        name=Label(frame,text='USER NAME',bg="grey",font=("times new roman",18,"bold"))
        name.place(x=10,y=90)

        self.name_text=Entry(frame, bd=0, bg="lightgrey", font=("times new roman",15))
        self.name_text.place(x=15,y=130)

        psw=Label(frame,text="PASSWORD",bg="grey", font=("times new roman",18,"bold"))
        psw.place(x=10,y=190)

        self.psw_txt=Entry(frame,bg="lightgrey",bd=0, font=("times new roman",15))
        self.psw_txt.place(x=10,y=230)

        btn1=Button(frame,text="LOGIN",cursor="hand2",command=self.data, font=("times new roman", 15),bg="grey",fg="black")
        btn1.place(x=150,y=270)

        btn=Button(frame,text="register new account....",command=self.window, cursor="hand2", bd=0,font=("times new roman", 10 ),bg="grey",fg="black")
        btn.place(x=10,y=325)

        btn2=Button(frame,text="next",command=self.window1, cursor="hand2", bd=0,font=("times new roman", 10 ),bg="grey",fg="black")
        btn2.place(x=300,y=325)

    def window(self):
        self.root.destroy()
        import new

    def window1(self):
        #self.root.destroy()
        import jnew

    def data(self):
        if self.name_text.get()=="" or self.psw_txt.get()=="":
            messagebox.showerror("Error","all fields are required")
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="patient")
                cur=con.cursor()
                cur.execute("select * from user where name=%s and psw=%s",(self.name_text.get(),self.psw_txt.get())),
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("error","invalid username and passowrd")
                else:
                    
                    messagebox.showinfo("success","welcome")
                    self.root.destroy()
                    import jupyt
                con.close()
            except Exception as es:
                messagebox.showerror("Error",f"Errordue to: {str(es)}")  

root=Tk()
obj=Register(root)
root.mainloop()