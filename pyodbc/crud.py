import pyodbc as odbc
from database import get_connection, get_cursor

connection = get_connection()
cursor = get_cursor(connection)

def create(connection):
    try:
        cursor = connection.cursor()
        table = """create table employee2 (id int primary key,name varchar(50),age int)"""
        cursor.execute(table)
        connection.commit()
        print("Table created successfully")
    except:
        print("Table already exits")

def insert(connection, id, name, age):
    insert_query = """insert into employee2 (id, name, age) values (?, ?, ?)"""
    cursor.execute(insert_query, (id, name, age))
    print("Values inserted successfully")

def update(connection, id, new_age):
    update_query = """update employee2 set age = ? where id = ?"""
    cursor.execute(update_query, (new_age, id))
    print("Value updated successfully")
    print("After Updation:")
    cursor.execute("select * from employee2")
    rows = cursor.fetchall()
    for i in rows:
        print(f"id = {i.id}, name = {i.name}, age = {i.age}")

def delete(connection, id):
    delete_query = "delete from employee2 where id = ?"
    cursor.execute(delete_query, (id,))
    connection.commit()
    print("Deleted successfully")
    cursor.execute("select * from employee2")
    rows = cursor.fetchall()
    for i in rows:
        print(f"id = {i.id}, name = {i.name}, age = {i.age}")

if __name__ == "__main__":
    create(connection)
    insert(connection, 1, 'Raj', 21)
    insert(connection, 2, 'Divya', 22)
    insert(connection, 3, 'Sruthi', 24)
    insert(connection, 4, 'Harish', 25)
    update(connection, 3, 29)
    delete(connection, 2)
