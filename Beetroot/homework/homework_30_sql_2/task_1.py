import sqlite3 as sq

with sq.connect('task1.sqlite') as conn:
    cur = conn.cursor()

    cur.execute("DROP TABLE IF EXISTS statements;")
    cur.execute("""CREATE TABLE IF NOT EXISTS statements (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        SQL_queries TEXT DEFAULT 'queries' NOT NULL);""")
    cur.execute("""INSERT INTO statements (SQL_queries)
        VALUES ("SELECT first_name, last_name, department_id, department_name
                   FROM employees INNER JOIN department USING (department_id);"),
               ("SELECT first_name, last_name, department_name, city, state_province
                   FROM employees e, department d, locations l
                   WHERE (e.department_id=d.department_id AND d.location_id=l.location_id);"),
               ("SELECT first_name, last_name, department_id, department_name
                   FROM employees INNER JOIN department USING (department_id)
                   WHERE department_id IN (40, 80);"),
               ("SELECT department_name FROM department;"),
               ("SELECT E.first_name AS 'Employee Name', M.first_name AS 'Manager'
                   FROM employees E JOIN employees M
                   ON E.manager_id = M.employee_id;"),
               ("SELECT job_title, first_name || ' ' ||last_name AS fullname,
                   (max_salary - salary) AS salary_difference
                   FROM jobs JOIN employees USING (job_id);"),
               ("SELECT jobs.job_title, (SELECT AVG(employees.salary)
                   FROM employees WHERE employees.job_id=jobs.job_id) AS avg_salary
                   FROM jobs WHERE avg_salary IS NOT NULL;"),
               ("SELECT e.first_name || ' ' ||e.last_name AS fullname, e.salary
                   FROM employees e, department d, locations l
                   WHERE e.department_id=d.department_id
                   AND d.location_id=l.location_id AND l.city='London';"),
               ("SELECT d.department_name, COUNT(e.first_name) AS number_of_employees
                   FROM department d INNER JOIN employees e
                   ON d.department_id = e.department_id GROUP BY d.department_name;")
               ;
               """)
