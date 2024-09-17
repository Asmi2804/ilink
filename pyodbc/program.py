import pyodbc as odbc
from database import get_connection,get_cursor
connection=get_connection()
cursor=get_cursor(connection)
def create():
    create_table_query = '''create table employee_info1 (employee_id int primary key,first_name varchar(50),last_name varchar(50),
    email varchar(100),phone_number varchar(15),job_title varchar(50),salary int)'''
    cursor.execute(create_table_query)
    connection.commit()
def insert():
    insert_query = '''insert into employee_info1 (employee_id, first_name, last_name, email, phone_number, job_title, salary) values
    (1, 'John', 'Doe', 'john.doe@example.com', '6234567890', 'Software Engineer', 75000),
    (2, 'Jane', 'Smith', 'jane.smith@example.com', '9345678901', 'Data Analyst', 68000),
    (3, 'Michael', 'Johnson', 'michael.johnson@example.com', '3456789012', 'Product Manager', 85000),
    (4, 'Emily', 'Davis', 'emily.davis@example.com', '6567890123', 'UX Designer', 70000),
    (5, 'Chris', 'Brown', 'chris.brown@example.com', '9678901234', 'System Administrator', 72000),
    (6, 'Sarah', 'Wilson', 'sarah.wilson@example.com', '6789012345', 'Marketing Specialist', 65000),
    (7, 'David', 'Taylor', 'david.taylor@example.com', '7890123456', 'Sales Manager', 90000),
    (8, 'Anna', 'Moore', 'anna.moore@example.com', '8901234567', 'HR Coordinator', 62000),
    (9, 'James', 'Anderson', 'james.anderson@example.com', '9012345678', 'Business Analyst', 73000),
    (10, 'Patricia', 'Thomas', 'patricia.thomas@example.com', '9123456789', 'Content Writer', 64000)'''
    cursor.execute(insert_query)
    connection.commit()
    

# max salary
a='''select max(salary) as maximum_salary from employee_info'''
cursor.execute(a)
max_salary=cursor.fetchall()
for i in max_salary:
    print(i)
      
# highest salary
b = '''select * from employee_info where salary >= (select avg(salary) from employee_info)'''
cursor.execute(b)
highest_salary= cursor.fetchall()
for i in highest_salary:
    print(i)

# like J
c='''select first_name,last_name from employee_info where first_name like 'J%' '''
cursor.execute(c)
print("name start with J")
name=cursor.fetchall()
for i in name:
    print(i)

# inner join
d='''select e2.name,em.first_name from employee_info as em inner join employee2 as e2 on e2.id=em.employee_id'''
cursor.execute(d)
print("inner join")
join=cursor.fetchall()
for i in join:
    print(i)

# RANK()
e='''select *,RANK() over(order by salary desc) from employee_info'''
cursor.execute(e)
print("Ranking")
rank=cursor.fetchall()
for i in rank:
    print(i)

# DENSE_RANK()
f='''select *,DENSE_RANK() over(order by salary desc) from employee_info'''
dense_rank=cursor.execute(f).fetchall()
print("Dense_rank")
for i in dense_rank:
    print(i)

cursor.close()
connection.close()  

