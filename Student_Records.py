# Import sqlite for data base
import sqlite3

# Create the SQLite database
# Set up a connection to the db and then a cursor to navigate it

connection = sqlite3.connect('student_records.db')
cursor = connection.cursor()

# Create a table students, to hold ID, name, and GPA
cursor.execute('''
               CREATE TABLE IF NOT EXISTS students (
               student_id   INTEGER PRIMARY KEY,
               first_name   TEXT    NOT NULL,
               last_name    TEXT    NOT NULL,
               email        TEXT    NOT NULL UNIQUE
               )
               ''')
connection.commit()

# Create our student database for all the classes taken by each student, and grade in each.
cursor.execute('''
                CREATE TABLE IF NOT EXISTS student_classes (
                class_id    INTEGER PRIMARY KEY,
                student_id  INTEGER     NOT NULL,
                class_name  TEXT        NOT NULL,
                FOREIGN KEY (student_id)
                    REFERENCES students (student_id)
                        ON UPDATE CASCADE
                        ON DELETE CASCADE
            )
''')

def add_student():
    # Create a students first and last names, and an email. Then add into the table students
    first_name = input("What is your students first name? ")
    last_name = input("What is the students last name? ")
    students_email = input("What is the email for your student?")
    cursor.execute('''
                   INSERT INTO students
                   (first_name, last_name, email)
                   VALUES (?, ?, ?)''',
                   (first_name, last_name, students_email)
                   )
    connection.commit()
    print("Student was added succesfully")

def get_students():
    cursor.execute('SELECT * FROM students')
    rows_students = cursor.fetchall()
    if not rows_students:
        print("There are no student yet, try adding one.")
        return

    print("The Students are as follows:")
    print("ID \t First Name \t Last Name \t Email")
    print("--------------------------------------------")

    for row in rows_students:
        print(f"{row[0]} \t {row[1]} \t {row[2]} \t {row[3]}")

    print()
    print()
    
# def add_class()

# def get_class()

# def generate_report()
    
def display_menu():
    print('Menu Options:')
    print("1. Add a new student")
    print("2. Display all students")
    print("3. Add a class a student has taken")
    print("4. Display all classes a student has taken")
    print("0. Exit the program")

done = False
while(not done):
    display_menu()
    choice = int(input("Enter your menu choice: "))
    match choice:
        case (1):
            # Add a Student
            add_student()
        case (2):
            # Display all the students
            get_students()
        case (0):
            # Exit Program
            done = True
        case _:
            print("Error, that is not one of the options listed")

# Close the database connection when we are done with the program
connection.close()


