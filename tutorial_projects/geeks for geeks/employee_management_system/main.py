#!/usr/bin/python3
# AUTH: https://www.geeksforgeeks.org/employee-management-system-using-python/
"""
This script provides functionality for managing employee
records in a MySQL database.
"""
import mysql.connector


# Establish connection to MySQL server
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    database="geeks_employee_management_system"
)


def Add_Employ():
    """
    Function to add a new employee to the database.
    """
    Id = input("Enter Employee Id : ")

    # Checking if Employee with given Id
    # Already Exist or Not
    if check_employee(Id):
        print("Employee already exists\nTry Again\n")
        menu()

    else:
        Name = input("Enter Employee Name : ")
        Post = input("Enter Employee Post : ")
        Salary = input("Enter Employee Salary : ")
        data = (Id, Name, Post, Salary)

        # Inserting Employee details in
        # the Employee Table
        sql = 'insert into empd values(%s,%s,%s,%s)'
        c = connection.cursor()

        # Executing the SQL Query
        c.execute(sql, data)

        # commit() method to make changes in
        # the table
        connection.commit()
        print("Employee Added Successfully ")
        menu()


def Promote_Employee():
    """
    Function to promote an employee by increasing their salary.
    """
    Id = int(input("Enter Employ's Id"))

    # Checking if Employee with given Id
    # Exist or Not
    if not check_employee(Id):
        print("Employee does not  exists\nTry Again\n")
        menu()
    else:
        Amount = int(input("Enter increase in Salary"))

        # Query to Fetch Salary of Employee
        # with given Id
        sql = 'select salary from empd where id=%s'
        data = (Id,)
        c = connection.cursor()

        # Executing the SQL Query
        c.execute(sql, data)

        # Fetching Salary of Employee with given Id
        r = c.fetchone()
        t = r[0]+Amount

        # Query to Update Salary of Employee with
        # given Id
        sql = 'update empd set salary=%s where id=%s'
        d = (t, Id)

        # Executing the SQL Query
        c.execute(sql, d)

        # commit() method to make changes in the table
        connection.commit()
        print("Employee Promoted")
        menu()


def Remove_Employ():
    """
    Function to remove an employee from the database.
    """
    Id = input("Enter Employee Id : ")

    # Checking if Employee with given Id Exist
    # or Not
    if not check_employee(Id):
        print("Employee does not  exists\nTry Again\n")
        menu()
    else:

        # Query to Delete Employee from Table
        sql = 'delete from empd where id=%s'
        data = (Id,)
        c = connection.cursor()

        # Executing the SQL Query
        c.execute(sql, data)

        # commit() method to make changes in
        # the table
        connection.commit()
        print("Employee Removed")
        menu()


def check_employee(employee_id):
    """
    Function to check if an employee exists in the database.
    """
    # Query to select all Rows f
    # rom employee Table
    sql = 'select * from empd where id=%s'

    # making cursor buffered to make
    # rowcount method work properly
    c = connection.cursor(buffered=True)
    data = (employee_id,)

    # Executing the SQL Query
    c.execute(sql, data)

    # rowcount method to find
    # number of rows with given values
    r = c.rowcount
    if r == 1:
        return True
    else:
        return False


def Display_Employees():
    """
    Function to display all employees in the database.
    """
    # query to select all rows from
    # Employee Table
    sql = 'select * from empd'
    c = connection.cursor()

    # Executing the SQL Query
    c.execute(sql)

    # Fetching all details of all the
    # Employees
    r = c.fetchall()
    for i in r:
        print("Employee Id : ", i[0])
        print("Employee Name : ", i[1])
        print("Employee Post : ", i[2])
        print("Employee Salary : ", i[3])
        print("---------------------\
        -----------------------------\
        ------------------------------\
        ---------------------")

    menu()


def menu():
    """
    Function to display the main menu for the employee management system.
    """
    print("Welcome to Employee Management Record")
    print("Press ")
    print("1 to Add Employee")
    print("2 to Remove Employee ")
    print("3 to Promote Employee")
    print("4 to Display Employees")
    print("5 to Exit")

    choice = int(input("Enter your Choice "))
    if choice == 1:
        Add_Employ()
    elif choice == 2:
        Remove_Employ()
    elif choice == 3:
        Promote_Employee()
    elif choice == 4:
        Display_Employees()
    elif choice == 5:
        exit(0)
    else:
        print("Invalid Choice")
        menu()


# Calling menu function
menu()
