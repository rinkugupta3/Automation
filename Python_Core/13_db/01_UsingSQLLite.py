# SQL Lite is lite weight database and doesn't require seperate server process 9serverless)
# CRUD - create (insert) read (select) update and delete
# cursor - cursor allows you to traverse or iterate over the rows retured when you use the select state
# sql statements - simple statements, prepared statements (database engine)


# If python want to use dedicate SQL server as odbc or rdbms and then use following.
# Install pip3 install pyobdc or pymsql
#import pyodbc
#import pymssql
#socketserverdatabase
#username
#password
#pyodbc.connect()

import sqlite3


# create the database
conn = sqlite3.connect('students_av.db')

# cursor object - cusor enbale t traverse along/over the data
cur = conn.cursor()

# Create the table = columns, data types and primary key
# Primary Key and Unique key- Primary can accept null value but unique doesn't
cur.execute("""
    CREATE TABLE IF NOT EXISTS student_table(
        id INTEGER PRIMARY KEY,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        email TEXT NULL UNIQUE,
        years_with_school INTEGER DEFAULT 0 
    )

""")

# insert - execute (for one transaction), executemany (for multiple transaction)
''''
cur.executemany("""
    INSERT INTO student_table(first_name,last_name,email,years_with_school)
    values(?,?,?,?)""",
                [
                    ('Dhiraj', 'Gupta', 'dg@abc.com', '1'),
                    ('John', 'Ed', 'john@abc.com', '3'),
                    ('Mike', 'YE', '', '4'),
                    ('Steve', 'Harding', 'steve@abc.com', '2')
                ]
                )
'''

conn.commit()

# read operation - select

#cur.execute("SELECT * FROM student_table where years_with_school > 2")
# simple statement to prepare statement
school = 2
cur.execute("SELECT * FROM student_table where years_with_school > ?", (school,))
rows = cur.fetchall()

for row in rows:
    print(row)
    #print(row[1])



for row in cur.execute('SELECT * FROM student_table order by years_with_school desc'):
    #print(row)
    #print(row[1])
    print(row[1], "has worked for ", row[4], "years with the school.")
    

cur.close()
conn.close()