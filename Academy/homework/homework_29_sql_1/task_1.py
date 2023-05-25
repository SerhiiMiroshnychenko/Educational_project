# Task 1

# Create a table
# Create a table of your choice inside the sample SQLite database,
# rename it, and add a new column. Insert a couple rows inside your table.
# Also, perform UPDATE and DELETE statements on inserted rows.
# As a solution to this task, create a file named: task1.sql,
# with all the SQL statements you have used to accomplish this task

import sqlite3 as sq

with sq.connect('task_1.sqlite') as conn:
    cur = conn.cursor()

    cur.execute("DROP TABLE IF EXISTS statements;")
    cur.execute("""CREATE TABLE IF NOT EXISTS statements (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        statment_name TEXT DEFAULT 'Statement' NOT NULL,
        statment_action TEXT DEFAULT 'Action' NOT NULL 
        );""")
    cur.execute("""INSERT INTO statements (statment_name, statment_action)
        VALUES ('DROP TABLE', 'Видалити таблицю'),
               ('CREATE TABLE', 'Створити таблицю'),
               ('INSERT INTO', 'Вставити данні в таблицю');
        """)
    cur.execute("""INSERT INTO statements (statment_name)
        VALUES ('UPDATE');
        """)
    cur.execute("""UPDATE statements
        SET statment_action = 'Оновити таблицю'
        WHERE id = 4;
        """)
    cur.execute("""INSERT INTO statements (statment_name, statment_action)
        VALUES ('DELETE FROM', 'Видалити данні з таблиці');
        """)
    cur.execute("""DELETE FROM statements
        WHERE id = 5;
        """)
    cur.execute("""INSERT INTO statements (statment_name)
        VALUES ('DELETE FROM');
        """)
    cur.execute("""UPDATE statements
        SET statment_action = 'Видалити данні з таблиці'
        WHERE id = 6;
        """)
