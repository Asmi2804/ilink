

import tkinter
from tkinter import *
from tkinter import messagebox
root=tkinter.Tk()
root.geometry("300x300")
#root.configure(bg="black")
root.title("Registration Form")
def Onclick_Submit():
    name=name_textbox.get()
    email=email_textbox.get()
    phone=phone_textbox.get()
    if name and email and phone:
        messagebox.showinfo("Status","Data Submitted")
    else:
        messagebox.showinfo("Status","Please fill all the fields")    

name_label=Label(root,text="Name :")
name_label.pack(anchor=tkinter.W,padx=10)
name_textbox=Entry()
name_textbox.pack(anchor=tkinter.W,padx=10)
email_label=Label(root,text="Email address :")
email_label.pack(anchor=tkinter.W,padx=10)
email_textbox=Entry()
email_textbox.pack(anchor=tkinter.W,padx=10)
phone_label=Label(root,text="Phone number :")
phone_label.pack(anchor=tkinter.W,padx=10)
phone_textbox=Entry()
phone_textbox.pack(anchor=tkinter.W,padx=10)
submit=Button(root,text="Submit",command=Onclick_Submit)
submit.pack(anchor=tkinter.W,padx=20)
root.mainloop()
