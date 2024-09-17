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
# database created
connection.execute('create database python')

# create table






