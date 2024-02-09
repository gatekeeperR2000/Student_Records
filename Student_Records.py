# Import sqlite for data base
import sqlite3

# Create the SQLite database
# Set up a connection to the db and then a cursor to navigate it

connection = sqlite3.connect('student_records.db')
cursor = connection.cursor()
cursor.execute('PRAGMA foreign_keys = ON')

# drop tables calls for debugging and resetting
cursor.execute('DROP TABLE IF EXISTS students')
cursor.execute('DROP TABLE IF EXISTS student_classes')

# Create a table students, to hold ID, name, and email
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
                grade       INTEGER     NOT NULL,
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
    print("The Students are as follows:")
    print("ID \t First Name \t Last Name \t Email")
    print("-----------------------------------------------") 

    rows = cursor.execute('SELECT student_id, first_name, last_name, email FROM students')
    debug_count = 0
    for row in rows:
        print(f"{row[0]} \t {row[1]} \t {row[2]} \t {row[3]}")
        print(debug_count)

    print()
    print()
    
def add_class():
    student_id = input("Enter the Student ID you wish to add a class under. ")

    # Try an exists command to see if the foreign key exists in students.
    rows = cursor.execute('SELECT first_name FROM students WHERE EXISTS (SELECT 1 FROM students WHERE student_id = ?)', (student_id))

    # Basic count to check if there is a row, so the foreign key exists. Otherwise we will get errors trying to insert later
    count = 0
    for row in rows:
        count += 1

    # Want to change this into an exists format, continue research
    if not count:
        print("Not a valid ID\n\n")
        return
    
    # We made it this far we should be good
    class_name = input("Enter the class name: ")
    grade = input("Enter the grade achieved: ")

    cursor.execute('''
                    INSERT INTO student_classes
                    (student_id, class_name, grade)
                    VALUES (?, ?, ?)''',
                    (student_id, class_name, grade))

def get_class():
    student_id = input("Enter the Students ID: ")
    print("classes are as follows\n")
    rows = cursor.execute('SELECT class_name, grade FROM student_classes WHERE student_id = ?', (student_id))

    for row in rows:
        print(f"{row[0]} \t {row[1]}")

    print()
    print()

def get_all_classes():
    rows = cursor.execute('SELECT class_id, student_id, class_name, grade FROM student_classes')
    print("Any classes found are listed below: ")
    for row in rows:
        print(f"{row[0]} \t {row[1]} \t {row[2]} \t {row[3]}")

    print("\n\n")


def generate_report():
    # Select first_name, last_name, class_name, and grade innerjoin studentid = studentid where student id = input
    student_id = input("Enter the ID for the student you wish to grab all class data for: ")
    rows = cursor.execute('''
                            SELECT
                                students.first_name,
                                students.last_name,
                                student_classes.class_name,
                                student_classes.grade
                            FROM
                                students
                                INNER JOIN student_classes ON students.student_id = student_classes.student_id
                                WHERE students.student_id = ?
                          ''', (student_id))
    for row in rows:
        print(f"{row[0]} \t {row[1]} \t {row[2]} \t {row[3]}")
    
    
def display_menu():
    print('Menu Options:')
    print("1. Add a new student")
    print("2. Display all students")
    print("3. Add a class a student has taken")
    print("4. Display all classes a student has taken")
    print("5. Display all classes on record for all students on record")
    print("6. generate a report of student and grades")
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
        case (3):
            # Add a class with a student ID
            add_class()
        case (4):
            # Get all classes attributed to student ID
            get_class()
        case (5):
            get_all_classes()
        case (6):
            generate_report()
        case (0):
            # Exit Program
            done = True
        case _:
            print("Error, that is not one of the options listed")

# Close the database connection when we are done with the program
connection.close()


