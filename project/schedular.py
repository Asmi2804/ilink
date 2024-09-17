from datetime import datetime, timedelta
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import threading
import pyodbc as odbc
import win32com.client as win32

def create_connection():
    connection = odbc.connect(
        'DRIVER={SQL Server};'
        'SERVER=DESKTOP-791PJFF\SQLEXPRESS01;'
        'DATABASE=master;'
        'Trust_Connection=yes;'
    )
    return connection

def create_database_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        use master;
        if not exists (select * from sysobjects where name='tasks' AND xtype='U')
        create table tasks (
            id int primary key identity,
            task_name varchar(100),
            task_description varchar(255),
            task_date datetime
        );
    ''')
    conn.commit()
    conn.close()
    

def insert():
    task_name = task_textbox.get()
    task_description = task_description_textbox.get()
    task_date_str = date_textbox.get()

    try:
        task_date = datetime.strptime(task_date_str, '%Y-%m-%d %H:%M:%S')
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD HH:MM:SS")
        return

    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        use master;
        insert into tasks (task_name, task_description, task_date) VALUES (?, ?, ?);
    ''', (task_name, task_description, task_date))
    conn.commit()
    conn.close()
    messagebox.showinfo("Success", "Task added successfully")
    schedule_reminder(task_date)

def send_reminder(task_name, task_description, task_date_str):
    olApp = win32.Dispatch('Outlook.Application')
    mail_item = olApp.CreateItem(0)
    mail_item.Subject = "Task Reminder: " + task_name
    mail_item.BodyFormat = 1
    mail_item.Body = f"Reminder for task:\n\n{task_name}\n\nDescription:\n{task_description}\n\nDue Date and Time:\n{task_date_str}"
    mail_item.Sender = "asmi.poomonijayanthi@ilink-systems.com"
    mail_item.To = "asmi.poomonijayanthi@ilink-systems.com"
    mail_item.Display()
    mail_item.Save()
    mail_item.Send()

def schedule_reminder(task_date):
    reminder_time = task_date - timedelta(minutes=10)
    delay = (reminder_time - datetime.now()).total_seconds()
    threading.Timer(delay, send_reminder, args=(task_textbox.get(), task_description_textbox.get(), task_date.strftime('%Y-%m-%d %H:%M:%S'))).start()

app = tk.Tk()
app.title("Task Scheduler")
app.geometry("300x200")

task_label = Label(app, text="Task Name :")
task_label.pack()
task_textbox = Entry()
task_textbox.pack()

task_description_label = Label(app, text="Task Description :")
task_description_label.pack()
task_description_textbox = Entry()
task_description_textbox.pack()

date_label = Label(app, text="Date (YYYY-MM-DD HH:MM:SS)")
date_label.pack()
date_textbox = Entry()
date_textbox.pack()

submit_button = Button(app, text="Add Task", command=insert)
submit_button.pack()

create_database_table()
app.mainloop()













