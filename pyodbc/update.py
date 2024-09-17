import pyodbc as obdc

DRIVER_NAME= 'SQL SERVER'
SERVER_NAME ='DESKTOP-791PJFF\SQLEXPRESS'
DATABASE_NAME ='master' 
con = f"""
    DRIVER={{{DRIVER_NAME}}};
    SERVER={SERVER_NAME};
    DATABASE = {DATABASE_NAME};
    Trust_Connection=yes;    
"""
connection = obdc.connect(con)
connection.autocommit=True
cursor=connection.cursor()
def update(connection, id, new_age):
    update_query = """update student set age = ? where id = ?"""
    cursor.execute(update_query, (new_age,id))
    print("Value Updated Successfully")
    print("After Updation:")
    cursor.execute("select * from student")
    rows = cursor.fetchall()
    for i in rows:
            print(f"id = {i.id}, name = {i.name}, age = {i.age}")


update(connection, 103, 29)
