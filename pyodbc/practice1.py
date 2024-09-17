import pyodbc as odbc
import tkinter
from tkinter import *
from tkinter import messagebox

def database_connection():
    DRIVER_NAME = 'SQL SERVER'
    SERVER_NAME = 'DESKTOP-791PJFF\SQLEXPRESS01'
    DATABASE_NAME = 'master'
    con = f"""
        DRIVER={{{DRIVER_NAME}}};
        SERVER={SERVER_NAME};
        DATABASE={DATABASE_NAME};
        Trust_Connection=yes;
        """
    connection=odbc.connect(con)
    connection.autocommit=True
    return connection
def Onclick():
    connection=database_connection()
    cursor=connection.cursor()
    name=name_textbox.get()
    email=email_textbox.get()
    password=password_textbox.get()
    query=("insert into login_page(login_name,login_email,login_password) values(?,?,?)")
    cursor.execute(query,(name,email,password))
    connection.commit
    messagebox.showinfo("Status","Data Submitted...")
    


app=tkinter.Tk()
app.title("Login Form")
app.geometry("300x200")
name_label=Label(app,text="Name :")
name_label.pack()
name_textbox=Entry(app)
name_textbox.pack()
email_label=Label(app,text="Email :")
email_label.pack()
email_textbox=Entry(app)
email_textbox.pack()
password_Label=Label(app,text="Password :")
password_Label.pack()
password_textbox=Entry(app,show="*")
password_textbox.pack()
submit=Button(app,text="Submit",command=Onclick)
submit.pack()

app.mainloop()

