# Import sqlite for data base
import sqlite3

# Create the SQLite database
# Set up a connection to the db and then a cursor to navigate it

connection = sqlite3.connect('student_records.db')
cursor = connection.cursor()

# Create a table students, to hold ID, name, and GPA
cursor.execute('''
               CREATE TABLE IF NOT EXISTS students (
               ID INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               gpa FLOAT
               )
               ''')
connection.commit()