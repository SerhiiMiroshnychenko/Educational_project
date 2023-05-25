# Task 2

# Select queries
# Use the sample SQLite database hr.db
# SQLite database hr.db link:
# Link to file

# As a solution to HW, create a file named:
# task2.sql with all SQL queries:
# write a query to display the names (first_name, last_name)
# using alias name "First Name", "Last Name" from the table of employees;
# write a query to get the unique department ID from the employee table
# write a query to get all employee details from the employee table
# ordered by first name, descending
# write a query to get the names (first_name, last_name), salary,
# PF of all the employees (PF is calculated as 12% of salary)
# write a query to get the maximum and minimum salary from the employees table
# write a query to get a monthly salary (round 2 decimal places)
# of each and every employee


import sqlite3 as sq

with sq.connect('hr.db') as conn:
    cur = conn.cursor()

    cur.execute("""SELECT first_name AS 'First Name',
     last_name AS 'Last Name' FROM employees;""")
    cur.execute("""SELECT DISTINCT department_id FROM employees;""")
    cur.execute("""SELECT * FROM employees ORDER BY first_name DESC;""")
    cur.execute("""SELECT first_name, last_name, salary, (salary * 0.12) as PF  FROM employees;""")
    cur.execute("""SELECT MAX(salary) FROM employees;""")
    cur.execute("""SELECT MIN(salary) FROM employees;""")
    cur.execute("""SELECT ROUND(salary/12.0, 2) AS monthly_salary FROM employees;""")
