import pyodbc as odbc
DRIVER_NAME= 'SQL SERVER'
SERVER_NAME ='DESKTOP-791PJFF\SQLEXPRESS'
DATABASE_NAME ='master' 
con= f"""
DRIVER={{{DRIVER_NAME}}};
SERVER={SERVER_NAME};
DATABASE={DATABASE_NAME};
Trust_Connection=yes;
"""
connection=odbc.connect(con)
connection.autocommit=True
crusor=connection.cursor()
def delete(connection,id):
    delete_query="delete from student where id=?"
    crusor.execute(delete_query,(id,))
    connection.commit
    print("Deleted Successfully\n")
    crusor.execute("select * from student")
    row=crusor.fetchall()
    for i in row:
        print(f"id ={i.id}, name={i.name}, age={i.age}")

delete(connection,102)        
