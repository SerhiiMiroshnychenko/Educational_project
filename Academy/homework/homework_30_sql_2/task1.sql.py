"""
Task 1

Joins
Use the sample SQLite database hr.db (same database you used in the previous
lesson for homework tasks)
As a solution to HW, create a file named: task1.sql with all SQL queries:
"""

import sqlite3 as sq

with sq.connect('hr.db') as conn:
    cur = conn.cursor()

    # 1. Write a query in SQL to display the first name, last name,
    # department number, and department name for each employee
    cur.execute("""SELECT first_name, last_name, department_id, department_name
                   FROM employees INNER JOIN department USING (department_id);""")

    # 2. Write a query in SQL to display the first and last name,
    # department, city, and state province for each employee
    cur.execute("""SELECT first_name, last_name, department_name, city, state_province
                   FROM employees e, department d, locations l
                   WHERE (e.department_id=d.department_id AND d.location_id=l.location_id);""")

    # 3. Write a query in SQL to display the first name, last name,
    # department number, and department name, for all employees
    # for departments 80 or 40
    cur.execute("""SELECT first_name, last_name, department_id, department_name
                   FROM employees INNER JOIN department USING (department_id)
                   WHERE department_id IN (40, 80);""")

    # 4. Write a query in SQL to display all departments including
    # those where does not have any employee
    cur.execute("""SELECT department_name FROM department;""")

    # 5. Write a query in SQL to display the first name of all employees
    # including the first name of their manager
    cur.execute("""SELECT E.first_name AS "Employee Name", M.first_name AS "Manager"
                   FROM employees E JOIN employees M
                   ON E.manager_id = M.employee_id;""")

    # 6. Write a query in SQL to display the job title, full name
    # (first and last name ) of the employee, and the difference
    # between the maximum salary for the job and the salary of the employee
    cur.execute("""SELECT job_title, first_name || ' ' ||last_name AS fullname,
                   (max_salary - salary) AS salary_difference
                   FROM jobs JOIN employees USING (job_id);""")


    # 7. Write a query in SQL to display the job title and the average
    # salary of employees
    cur.execute("""SELECT jobs.job_title, (SELECT AVG(employees.salary)
                   FROM employees WHERE employees.job_id=jobs.job_id) AS avg_salary
                   FROM jobs WHERE avg_salary IS NOT NULL;""")


    # 8. Write a query in SQL to display the full name (first and last name),
    # and salary of those employees who work in any department located in London
    cur.execute("""SELECT e.first_name || ' ' ||e.last_name AS fullname, e.salary
                   FROM employees e, department d, locations l
                   WHERE e.department_id=d.department_id
                   AND d.location_id=l.location_id AND l.city='London';""")



    # 9. Write a query in SQL to display the department name and the number of
    # employees in each department
    cur.execute("""SELECT d.department_name, COUNT(e.first_name) AS number_of_employees
                   FROM department d INNER JOIN employees e
                   ON d.department_id = e.department_id GROUP BY d.department_name;""")
