-- AUTH: codenvibes
-- DESC: A script to create a database and table for employee management system

CREATE DATABASE IF NOT EXISTS geeks_employee_management_system;
USE geeks_employee_management_system;
CREATE TABLE IF NOT EXISTS empd (
    id INT PRIMARY KEY,
    name VARCHAR(255),
    post VARCHAR(255),
    salary DECIMAL(10, 2)
)
