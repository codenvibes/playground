from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# Establish connection to MySQL server
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    database="geeks_employee_management_system"
)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/add_employee', methods=['POST'])
def add_employee():
    Id = request.form['Id']

    if check_employee(Id):
        return "Employee already exists. Try again."

    Name = request.form['Name']
    Post = request.form['Post']
    Salary = request.form['Salary']
    data = (Id, Name, Post, Salary)

    sql = 'insert into empd values(%s,%s,%s,%s)'
    c = connection.cursor()
    c.execute(sql, data)
    connection.commit()
    return "Employee Added Successfully."

@app.route('/remove_employee', methods=['POST'])
def remove_employee():
    Id = request.form['Id']

    if not check_employee(Id):
        return "Employee does not exist."

    sql = 'delete from empd where id=%s'
    data = (Id,)
    c = connection.cursor()
    c.execute(sql, data)
    connection.commit()
    return "Employee Removed."

@app.route('/promote_employee', methods=['POST'])
def promote_employee():
    Id = request.form['Id']
    Amount = int(request.form['Amount'])

    if not check_employee(Id):
        return "Employee does not exist."

    sql = 'select salary from empd where id=%s'
    data = (Id,)
    c = connection.cursor()
    c.execute(sql, data)
    r = c.fetchone()
    t = r[0]+Amount

    sql = 'update empd set salary=%s where id=%s'
    d = (t, Id)
    c.execute(sql, d)
    connection.commit()
    return "Employee Promoted."

@app.route('/display_employees')
def display_employees():
    sql = 'select * from empd'
    c = connection.cursor()
    c.execute(sql)
    r = c.fetchall()
    employees = []
    for i in r:
        employee = {
            'Id': i[0],
            'Name': i[1],
            'Post': i[2],
            'Salary': i[3]
        }
        employees.append(employee)
    return render_template('employees.html', employees=employees)

def check_employee(employee_id):
    sql = 'select * from empd where id=%s'
    c = connection.cursor(buffered=True)
    data = (employee_id,)
    c.execute(sql, data)
    r = c.rowcount
    if r == 1:
        return True
    else:
        return False

if __name__ == '__main__':
    app.run(debug=True)
