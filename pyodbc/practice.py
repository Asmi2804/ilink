import pyodbc as odbc
DRIVER_NAME= 'SQL SERVER'
SERVER_NAME ='DESKTOP-791PJFF\SQLEXPRESS'
DATABASE_NAME ='master' 
con=f"""
DRIVER={{{DRIVER_NAME}}};
SERVER={SERVER_NAME};
DATABASE={DATABASE_NAME};
Trusted_Connection=yes;
"""
connection=odbc.connect(con)
connection.autocommit=True
cursor=connection.cursor()
single_row=cursor.execute("select id from student").fetchone()
all_row=cursor.execute("select * from student").fetchall()
specific_row=cursor.execute("select name from student").fetchmany(2)
print(specific_row)