# As a solution to HW, create a file named:
# task2.sql with all SQL queries from Task 2

import sqlite3 as sq

with sq.connect('task2.sqlite') as conn:
    cur = conn.cursor()

    cur.execute("DROP TABLE IF EXISTS statements;")
    cur.execute("""CREATE TABLE IF NOT EXISTS statements (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        SQL_queries TEXT DEFAULT 'queries' NOT NULL);""")
    cur.execute("""INSERT INTO statements (SQL_queries)
        VALUES ("SELECT first_name AS 'First Name', last_name AS 'Last Name' FROM employees;"),
               ("SELECT DISTINCT department_id FROM employees;"),
               ("SELECT * FROM employees ORDER BY first_name DESC;"),
               ("SELECT first_name, last_name, salary, (salary * 0.12) as PF  FROM employees;"),
               ("SELECT MAX(salary) FROM employees;"),
               ("SELECT MIN(salary) FROM employees;"),
               ("SELECT ROUND(salary/12.0, 2) AS monthly_salary FROM employees;");
               """)
