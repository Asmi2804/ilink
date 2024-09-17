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

def create_table(connection):
    table = """
    create table student(id int primary key,name varchar(50),age int)"""
    cursor.execute(table)
    print("Table created successfully")

create_table(connection)
