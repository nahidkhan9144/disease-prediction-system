#https://www.munotes.in/bscit-sem6-question-paper.html


from tkinter import *
from tkinter import ttk, messagebox
from PIL import ImageTk, Image
import pymysql
class Regnew:
    def __init__(self,root):
        self.root=root
        self.root.title('FOR NEW USER')
        self.root.geometry('1350x1875+0+0')
        self.root.configure(bg="white")
        self.root.resizable(True,True)


        self.img= ImageTk.PhotoImage(Image.open('D:\\python programming\\img\\virus.JFIF'))
        
        
        tit=Label(text='DISEASE PREDICTION SYSTEM',bg="lightgrey", font=("times new roman",30,"bold"))
        tit.place(x=400,y=5)
        title=Label(text='create new account',bg="lightgrey", font=("times new roman",15,"bold"))
        title.place(x=600,y=80)
        #self.bg = ImageTk.PhotoImage(file="img/sun.png")
        #bg=Label(self.root,image=self.bg).place(x=250,y=0,relwidth=1,relheight=1)

        frame=Frame(root,width=400,height=400,bg="lightgrey")
        frame.place(x=500,y=180)

        heading=Label(frame,text='SIGN IN',bg="lightgrey", font=("times new roman",25,"bold"))
        heading.place(x=150,y=5)

        name=Label(frame,text='USER NAME', bg="lightgrey",font=("times new roman",15,"bold"))
        name.place(x=10,y=90)
        self.name_text=Entry(frame, bd=0, bg="white", font=("times new roman",15))
        self.name_text.place(x=15,y=120)
        contact=Label(frame,text='MOBILE NUMBER', bg="lightgrey",font=("times new roman",15,"bold"))
        contact.place(x=15,y=170)
        self.contact_text=Entry(frame, bd=0, bg="white", font=("times new roman",15))
        self.contact_text.place(x=15,y=200)
        
        psw=Label(frame,text="PASSWORD",bg="lightgrey", font=("times new roman",15,"bold"))
        psw.place(x=15,y=250)

        self.psw_txt=Entry(frame,bg="white",bd=0, font=("times new roman",15))
        self.psw_txt.place(x=15,y=280)

        btn=Button(frame,text="REGISTER",cursor="hand2",command=self.data,bd=4,font=("times new roman", 15),bg="grey",fg="black")
        btn.place(x=150,y=320)

        btn1=Button(frame,text="already have an account.....",command=self.window,cursor="hand2",bd=1,font=("times new roman", 10),bg="lightgrey",fg="black")
        btn1.place(x=5  ,y=370)

    def window(self):
        self.root.destroy()
        import dis

    def data(self):
        if self.name_text.get()=="" or self.psw_txt.get()=="" or self.contact_text.get=="":
            messagebox.showerror("Error","all fields are required")
        #elif self.pass_txt.get()==len(10):
            #messagebox.showerror("Error","length should be 10")
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="patient")
                cur=con.cursor()
                cur.execute("insert into user(name,contact,psw) values(%s,%s,%s)",
                        (self.name_text.get(),
                        self.contact_text.get(),
                        self.psw_txt.get()
                        ) )
                con.commit()
                messagebox.showinfo("success","register successfully")
            except Exception as es:
                messagebox.showerror("Error",f"Errordue to: {str(es)}")  
root=Tk()
obj=Regnew(root)
root.mainloop()
