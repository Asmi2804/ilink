import pyodbc
import tkinter as tk
from tkinter import messagebox
import requests
from datetime import datetime,date
import threading
import multiprocessing
import time


def create_connection():
    connection = pyodbc.connect(
        'DRIVER={SQL Server};'
        'SERVER=DESKTOP-791PJFF\SQLEXPRESS01;'
        'DATABASE=master;'
        'Trust_Connection=yes;'
        
    )
    return connection

def create_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE  tasks1 (
            id INT PRIMARY KEY IDENTITY(1,1),
            task_name VARCHAR(100),
            task_description VARCHAR(255),
            due_date DATE,
            status VARCHAR(50)
        )
    ''')
    conn.commit()
    conn.close()

# create_table()


def add_task():
    task_name = task_name_entry.get()
    task_description = task_description_entry.get()
    due_date = due_date_entry.get()
    if task_name and due_date:
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO tasks1 (task_name, task_description, due_date, status)
            VALUES (?, ?, ?, ?)
        ''', (task_name, task_description, due_date, 'Pending'))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Task added successfully")
        task_name_entry.delete(0, tk.END)
        task_description_entry.delete(0, tk.END)
        due_date_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter task name and due date")

app = tk.Tk()
app.title("Task Scheduler")

tk.Label(app, text="Task Name").grid(row=0)
tk.Label(app, text="Task Description").grid(row=1)
tk.Label(app, text="Due Date").grid(row=2)

task_name_entry = tk.Entry(app)
task_description_entry = tk.Entry(app)
due_date_entry = tk.Entry(app)

task_name_entry.grid(row=0, column=1)
task_description_entry.grid(row=1, column=1)
due_date_entry.grid(row=2, column=1)

tk.Button(app, text="Add Task", command=add_task).grid(row=3, column=1)

app.mainloop()


def fetch_task_details(task_id):
    response = requests.get(f'https://api.example.com/tasks/{task_id}')
    if response.status_code == 200:
        return response.json()
    else:
        return None
    
def get_due_tasks():
    conn = create_connection()
    cursor = conn.cursor()
    today=date.today()
    cursor.execute('SELECT * FROM tasks1 WHERE due_date <= ? AND status = ?', (today, 'Pending'))
    due_tasks = cursor.fetchall()
    conn.close()
    return due_tasks


def check_due_tasks():
    while True:
        due_tasks = get_due_tasks()
        for task in due_tasks:
            print(f"Task {task[1]} is due!")
        time.sleep(60)  
def process_task(task_id):
    task_details = fetch_task_details(task_id)
    if task_details:
        print(f"Processing task {task_details['name']}")

if __name__ == "__main__":
    threading.Thread(target=check_due_tasks).start()
    task_id_list = [1, 2, 3, 4]  
    with multiprocessing.Pool() as pool:
        pool.map(process_task, task_id_list)
