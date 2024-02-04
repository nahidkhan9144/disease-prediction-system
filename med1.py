from tkinter import *
from tkinter import Tk
from tkinter import ttk
from tkinter import filedialog
import pandas as pd
class datas:
    def __init__(self,app):
        self.app=app
        #self.app = Tk()
        self.app.title('Test')
        self.app.geometry('1300x3100')
        t1=Label(app,text="search",bg="lightgrey",font=("times new roman", 15))
        t1.place(x=70,y=50)
        e1=Entry(app,width=35,bg="lightgrey",bd=0, font=("times new roman",15))
        e1.place(x=150,y=50)
        btn3=Button(text="search",cursor="hand2",command=lambda:filen(),font=("times new roman", 15),bg="white",fg="black")
        btn3.place(x=530,y=40)

        df=pd.read_csv("d:/med/medicine.csv")
        #pd.set_option('display.max_rows', 100)
        #t1.insert(END,df.head(100),"center")
        def filen():
            l1=list(df)
            query=e1.get().strip()
            if query.isdigit():
                str1=df['price']==int(query)
            else:
                str1=df.name.str.contains(query,case=False)
            df2=df[(str1)]
            rset=df2.to_numpy().tolist()
            trv=ttk.Treeview(app,selectmode='browse')
            #trv.place(x=100,y=150)
            trv.grid(row=1000,column=2,columnspan=1,padx=30,pady=90)
            trv['height']=25
            trv['show']='headings'
            trv['columns']=l1
            for i in l1:
                trv.column(i,width=190,anchor='c')
                trv.heading(i,text=i)
            for dt in rset:
                v=[r for r in dt]
                trv.insert("",'end',iid=v[0],values=v)
    #self.app.mainloop()
app=Tk()
obj=datas(app)
app.mainloop()