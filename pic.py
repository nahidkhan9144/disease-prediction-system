from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image,ImageTk

root=Tk()
root.title('login')
root.geometry('700x500')

#frame = Frame(root, x=50, y=700,width=600, height=400)
#frame.pack()
#frame.place(anchor='center', relheight=1, relwidth=1)

img= ImageTk.PhotoImage(Image.open('D:\\python programming\\img\\sun.png'))
label=Label(root,image=img)
label.pack()
#root.resizable(True,True)


root.mainloop()