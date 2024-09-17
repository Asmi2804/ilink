import tkinter
from tkinter import *

root=tkinter.Tk()
root.geometry("300x300")
root.title("Login Form")
login=Label(root,text="Login")
name_label=Label(root,text="Enter Username :")
name_textbox=Entry()
email_label=Label(root,text="Enter Email id :")
email_textbox=Entry(root,show="*")
submit=Button(root,text="Submit")
login.grid(row=0,column=0,columnspan=2)
name_label.grid(row=1,column=0)
name_textbox.grid(row=1,column=1)
email_label.grid(row=2,column=0)
email_textbox.grid(row=2,column=1)
submit.grid(row=3,column=0,columnspan=2)

root.mainloop()