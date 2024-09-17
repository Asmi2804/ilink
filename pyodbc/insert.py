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
def insert(connection, id, name, age):
    insert_query = """insert into student(id, name, age) values (?, ?, ?)"""
    cursor.execute(insert_query, (id, name, age))
    print("Values inserted successfully")
insert(connection,101,'Raj',21) 
insert(connection,102,'Swetha',22) 
insert(connection,103,'Sruthi',24) 
insert(connection,104,'harish',25)
