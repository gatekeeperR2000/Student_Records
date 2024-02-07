# Import sqlite for data base
import sqlite3

# Create the SQLite database
# Set up a connection to the db and then a cursor to navigate it

connection = sqlite3.connect('student_records.db')
cursor = connection.cursor()

# Create a table students, to hold ID, name, and GPA
cursor.execute('''
               CREATE TABLE IF NOT EXISTS students (
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               gpa FLOAT
               )
               ''')
connection.commit()

# def add_student()

# def get_student()
    
# def update_gpa()

# def get_gpa()

# def generate_report()
    
# def display_menu()

done = False
while(not done):
    # display_menu()
    choice = int(input("Enter your menu choice: "))
    match choice:
        case (1):
            # Add a Student
            print(1)
        case (2):
            # update a students GPA
            print(2)
        case (0):
            # Exit Program
            done = True
        case _:
            print("Error")


