<h1 align="center"><b>EMPLOYEE MANAGEMENT SYSTEM USING PYTHON</b></h1>
<div align="center"><code>python</code> <code>mysqlconnector</code></div>

<br>

## Definitions
<details>
<summary><b><a href=" "> </a>mysqlconnector</b></summary><br>

***MySQL Connector/Python enables Python applications to connect to MySQL databases, allowing you to interact with MySQL databases from your Python code.*** It provides an interface for executing SQL queries, managing database connections, and handling data retrieval and manipulation. This connector is an official MySQL driver for Python and is maintained by the MySQL development team. It supports various features of MySQL, including transactions, stored procedures, prepared statements, and more.

<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a></b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a></b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a></b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a></b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<!-- <br>

## Background Context -->


<!-- <br>
<hr>
<h3><a href=>Notes</a></h3>
<hr> -->

<!-- <br>

## Resources
<details>
<summary><b><a href=" "> </a></b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a></b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a></b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a></b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a></b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details> -->


<!-- <br>

**man or help:**
- `` -->

<br>

The task is to create a Database-driven Employee Management System in Python that will store the information in the MySQL Database. The script will contain the following operations :

- Add Employee
- Remove Employee
- Promote Employee
- Display Employees

The idea is that we perform different changes in our Employee Record by using different functions for example the Add_Employee will insert a new row in our Employee, also, we will create a Remove Employee Function which will delete the record of any particular existing employee in our Employee table. This System works on the concepts of taking the information from the database making required changes in the fetched data and applying the changes in the record which we will see in our Promote Employee System. We can also have the information about all the existing employees by using the Display Employee function. The main advantage of connecting our program to the database is that the information becomes lossless even after closing our program a number of times.

## Getting Started
For creating the Employee Management System in Python that uses MySQL database we need to connect Python with MySQL.

For making a connection we need to install `mysqlconnector` which can be done by writing the following command in the command prompt on Windows.
```
pip install mysqlconnector
```
Now after successful installation of mysqlconnector we can connect MySQL with Python which can be done by writing the following code 
```Python
import mysql.connector

con = mysql.connector.connect(
    host="localhost", user="root", password="password", database="emp")
```
Now we are Done with the connections, so we can focus on our Employee Management System 

### Table in Use:
Employee Record

The idea is that we keep all the information about the Employee in the above table and manipulate the table whenever required. So now we will look at the working of each operation in detail.

Check Employee Function
The check employee function takes employee id as a parameter and checks whether any employee with given id exists in the employee details record or not. For checking this it uses cursor.rowcount() function which counts the number of rows that match with given details. It is a utility function, and we will see its use in later operations like Add employee function, etc.

Program:

Python3
# Function To Check if Employee with
# given Id Exist or Not
 
def check_employee(employee_id):
 
    # Query to select all Rows f
    # rom employee Table
    sql = 'select * from empd where id=%s'
 
    # making cursor buffered to make
    # rowcount method work properly
    c = con.cursor(buffered=True)
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
Add Employee Function
The Add Employee function will ask for the Employee Id and uses the check employee function to check whether the employee to be added already exist in our record or not if employee details do not already exist then it asks for details of the employee to be added like Employee Name, Post of Employee and Salary of the employee. Now after getting all such details from the user of that system it simply inserts the information in our Employee details table.

Program:

Python3
# Function to mAdd_Employee
 
def Add_Employ():
 
    Id = input("Enter Employee Id : ")
 
    # Checking if Employee with given Id
    # Already Exist or Not
    if(check_employee(Id) == True):
        print("Employee already exists\nTry Again\n")
        menu()
     
    else:
        Name = input("Enter Employee Name : ")
        Post = input("Enter Employee Post : ")
        Salary = input("Enter Employee Salary : ")
        data = (Id, Name, Post, Salary)
 
        # Inserting Employee details in the Employee 
        # Table
        sql = 'insert into empd values(%s,%s,%s,%s)'
        c = con.cursor()
 
        # Executing the SQL Query
        c.execute(sql, data)
 
        # commit() method to make changes in the table
        con.commit()
        print("Employee Added Successfully ")
        menu()
Remove Employee Function
The Remove Employee Function will simply ask for Id of the employee to be removed because Id is Primary key in our Employee Details Record as there can be two employees with the same name, but they must have a unique id. The Remove Employee function uses the check employee function to check whether the employee to be removed exists in our record or not if employee details exist then after getting a valid employee id it deletes the record corresponding to that employee id.

Program

Python3
# Function to Remove Employee with given Id
def Remove_Employ():
    Id = input("Enter Employee Id : ")
 
    # Checking if Employee with given Id
    # Exist or Not
    if(check_employee(Id) == False):
        print("Employee does not  exists\nTry Again\n")
        menu()
     
    else:
         
        # Query to Delete Employee from Table
        sql = 'delete from empd where id=%s'
        data = (Id,)
        c = con.cursor()
 
        # Executing the SQL Query
        c.execute(sql, data)
 
        # commit() method to make changes in 
        # the table
        con.commit()
        print("Employee Removed")
        menu()
Promote Employee Function
The Promote Employee function will ask for the Employee Id and uses the check employee function to check whether the employee to be Promoted exist in our record or not if employee details exist then it will ask for the amount by which his salary is to be increased. After getting the valid details it increases the salary of the employee with the given id by the given amount.

Program

Python3
# Function to Promote Employee
def Promote_Employee():
    Id = int(input("Enter Employ's Id"))
 
    # Checking if Employee with given Id
    # Exist or Not
    if(check_employee(Id) == False):
        print("Employee does not  exists\nTry Again\n")
        menu()
    else:
        Amount = int(input("Enter increase in Salary"))
 
        # Query to Fetch Salary of Employee with 
        # given Id
        sql = 'select salary from empd where id=%s'
        data = (Id,)
        c = con.cursor()
 
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
        con.commit()
        print("Employee Promoted")
        menu()
Display Employees Function
The Display Employees function is simply a select query of SQL which fetches all the records stored in the employee details table and prints them line by line.

Program:

Python3
# Function to Display All Employees
# from Employee Table
 
def Display_Employees():
     
    # query to select all rows from
    # Employee Table
    sql = 'select * from empd'
    c = con.cursor()
     
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
        print("-----------------------------\
        -------------------------------------\
        -----------------------------------")
    menu()
 
 

Menu Function
 

The Menu function displays the menu to the user and asks the user to enter his choice for performing operations like Add employee, Remove employee, etc.

 

Program

 

Python3
# menu function to display the menu
def menu():
    print("Welcome to Employee Management Record")
    print("Press ")
    print("1 to Add Employee")
    print("2 to Remove Employee ")
    print("3 to Promote Employee")
    print("4 to Display Employees")
    print("5 to Exit")
     
    # Taking choice from user
    ch = int(input("Enter your Choice "))
    if ch == 1:
        Add_Employ()
         
    elif ch == 2:
        Remove_Employ()
         
    elif ch == 3:
        Promote_Employee()
         
    elif ch == 4:
        Display_Employees()
         
    elif ch == 5:
        exit(0)
         
    else:
        print("Invalid Choice")
        menu()
Complete Code:

Python3
# importing mysql connector
import mysql.connector
 
# making Connection
con = mysql.connector.connect(
    host="localhost", user="root", password="password", database="emp")
 
# Function to mAdd_Employee
def Add_Employ():
 
    Id = input("Enter Employee Id : ")
     
    # Checking if Employee with given Id 
    # Already Exist or Not
    if(check_employee(Id) == True):
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
        c = con.cursor()
         
        # Executing the SQL Query
        c.execute(sql, data)
         
        # commit() method to make changes in
        # the table
        con.commit()
        print("Employee Added Successfully ")
        menu()
 
# Function to Promote Employee
def Promote_Employee():
    Id = int(input("Enter Employ's Id"))
     
    # Checking if Employee with given Id 
    # Exist or Not
    if(check_employee(Id) == False):
        print("Employee does not  exists\nTry Again\n")
        menu()
    else:
        Amount = int(input("Enter increase in Salary"))
         
        # Query to Fetch Salary of Employee 
        # with given Id
        sql = 'select salary from empd where id=%s'
        data = (Id,)
        c = con.cursor()
         
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
        con.commit()
        print("Employee Promoted")
        menu()
 
# Function to Remove Employee with given Id
def Remove_Employ():
    Id = input("Enter Employee Id : ")
     
    # Checking if Employee with given Id Exist
    # or Not
    if(check_employee(Id) == False):
        print("Employee does not  exists\nTry Again\n")
        menu()
    else:
         
        # Query to Delete Employee from Table
        sql = 'delete from empd where id=%s'
        data = (Id,)
        c = con.cursor()
         
        # Executing the SQL Query
        c.execute(sql, data)
         
        # commit() method to make changes in 
        # the table
        con.commit()
        print("Employee Removed")
        menu()
 
 
# Function To Check if Employee with
# given Id Exist or Not
def check_employee(employee_id):
     
    # Query to select all Rows f
    # rom employee Table
    sql = 'select * from empd where id=%s'
     
    # making cursor buffered to make
    # rowcount method work properly
    c = con.cursor(buffered=True)
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
 
# Function to Display All Employees
# from Employee Table
def Display_Employees():
     
    # query to select all rows from 
    # Employee Table
    sql = 'select * from empd'
    c = con.cursor()
     
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
 
# menu function to display menu
def menu():
    print("Welcome to Employee Management Record")
    print("Press ")
    print("1 to Add Employee")
    print("2 to Remove Employee ")
    print("3 to Promote Employee")
    print("4 to Display Employees")
    print("5 to Exit")
 
    ch = int(input("Enter your Choice "))
    if ch == 1:
        Add_Employ()
    elif ch == 2:
        Remove_Employ()
    elif ch == 3:
        Promote_Employee()
    elif ch == 4:
        Display_Employees()
    elif ch == 5:
        exit(0)
    else:
        print("Invalid Choice")
        menu()
 
 
# Calling menu function
menu()
Output

