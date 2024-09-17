from flask import Flask, jsonify, request
import pyodbc as odbc
from database import get_connection, get_cursor

connection = get_connection()
cursor = get_cursor(connection)


class create_api_connection():
    def get_value(self):
        cursor.execute("select * from employee_info1")
        rows = cursor.fetchall()
        result = []
        columns = [column[0] for column in cursor.description]
        for row in rows:
            row_dict = dict(zip(columns, row))
            result.append(row_dict)
        return jsonify(columns)
    
    def insert_value(self):
        data = request.get_json()
        id = data.get('employee_id')
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        email=data.get('email')
        phone_number=data.get('phone_number')
        job_title=data.get('job_title')
        salary=data.get('salary')
        query="""insert into employee_info1 (employee_id, first_name, last_name,email,phone_number,job_title,salary) VALUES (?, ?, ?,?,?,?,?)"""
        try:
            cursor.execute(query, (id, first_name, last_name,email,phone_number,job_title,salary))
            connection.commit()
            response='Data inserted successfully'
        except:
            connection.rollback()
            response='Error in inserting data'
        return jsonify(response)
    
    def update_value(self):
        data = request.get_json()
        employee_id = data.get('employee_id')
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        email = data.get('email')
        phone_number = data.get('phone_number')
        job_title = data.get('job_title')
        salary = data.get('salary')
        query = """update employee_info1
                   set first_name = ?, last_name = ?, email = ?, phone_number = ?, job_title = ?, salary = ?
                   where employee_id = ?"""
        
        try:
            cursor.execute(query, (first_name, last_name, email, phone_number, job_title, salary, employee_id))
            connection.commit()
            response='Data Updated Successfully'
        except:
            connection.rollback()
            response='Error in Updating data'
        return jsonify(response)
    
    def delete_value(self):
        data = request.get_json()
        employee_id = data.get('employee_id')
        query = """delete from employee_info1 where employee_id = ?"""
        try:
            cursor.execute(query, employee_id)
            connection.commit()
            response='Data Deleted successfully'
        except:
            connection.rollback()
            response='Error in Deleting data'
        return jsonify(response)

    
app = Flask(__name__)
obj = create_api_connection()

@app.route('/')
def new():
    return "Welcome to Flask"

@app.route('/items', methods=['GET'])
def get_items():
    return obj.get_value()

@app.route('/items', methods=['POST'])
def add_item():
    return obj.insert_value()

@app.route('/items/<int:employee_id>', methods=['PUT'])
def update_item(employee_id):
    return obj.update_value()

@app.route('/items', methods=['DELETE'])
def delete_item():
    return obj.delete_value()

if __name__ == '__main__':
    app.run(debug=True)

















