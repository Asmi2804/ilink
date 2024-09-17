import tkinter
from tkinter import *
from tkinter import messagebox
import re
import pyodbc as odbc

DRIVER_NAME= 'SQL SERVER'
SERVER_NAME ='DESKTOP-791PJFF\SQLEXPRESS'
DATABASE_NAME ='python' 

con = f"""
    DRIVER={{{DRIVER_NAME}}};
    SERVER={SERVER_NAME};
    DATABASE = {DATABASE_NAME};
    Trust_Connection=yes;    
"""
connection = odbc.connect(con)
connection.autocommit=True
cursor=connection.cursor()

def insert_value(name,email,phone):
    #print(name ,email,phone)
    try:
        # a="asmi"
        # b="asmi@gmail.com"
        # c="123456777"
        # cursor.execute("insert into registartion values(?,?,?)",(a,b,c))
        # cursor.close()
        # connection.close()
        cursor.execute("INSERT INTO registration VALUES ('asmi', 'asmi@gmail.com', '123456777')") 
        connection.commit()  
        cursor.close()
    except (Exception, odbc.Error) as error:
        print("Error while Inserting data into SQL Server:", error)   
    



root=tkinter.Tk()
root.title("Registration form")
root.geometry("300x300")

def validate_name(name):
    return len(name)>0

def validate_email(email):
    e=r'^[a-zA-Z0-9_.±]+@[a-zA-Z0-9-]+.[a-zA-Z0-9-.]+$'
    return re.match(e,email) is not None

def validate_phone(phone):
    p=r'^\d{10}$'
    return re.match(p,phone) is not None

def Onclick():
    name=name_textbox.get()
    email=email_textbox.get()
    phone=phone_textbox.get()

    if not validate_name(name):
        messagebox.showinfo("Status","Enter a valid name")
        return
    
    if not validate_email(email):
        messagebox.showinfo("Status","Enter a valid gmail address")
        return
    
    if not validate_phone(phone):
        messagebox.showinfo("Status","Enter a valid phone number")
        return
    
    if insert_value(name,email,phone):
        messagebox.showinfo("Status","Data Submited")
    else:
        messagebox.showinfo("Status","Error in submitting")    
    

name_label=Label(root,text="Name :")
name_label.pack()
name_textbox=Entry()
name_textbox.pack()
email_label=Label(root,text="Email :")
email_label.pack()
email_textbox=Entry()
email_textbox.pack()
phone_label=Label(root,text="Phone number")
phone_label.pack()
phone_textbox=Entry()
phone_textbox.pack()
submit=Button(root,text="Submit",command=Onclick)
submit.pack()











root.mainloop()