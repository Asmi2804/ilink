import pyodbc as odbc

def get_connection():
    DRIVER_NAME = 'SQL SERVER'
    SERVER_NAME = 'DESKTOP-791PJFF\SQLEXPRESS01'
    DATABASE_NAME = 'master'
    con = f"""
        DRIVER={{{DRIVER_NAME}}};
        SERVER={SERVER_NAME};
        DATABASE={DATABASE_NAME};
        Trust_Connection=yes;
        """
    connection = odbc.connect(con)
    connection.autocommit = True
    return connection

def get_cursor(connection):
    return connection.cursor()
