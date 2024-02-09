# Overview

This is a simple Python program ustilizing SQLite3. I wanted to study up on SQL and chose python and SQLite3 as my medium for showing some of what I had learned. I wanted to spend two weeks learning SQL reltional databases and feel that I have a basic understanding of how they work. With time I plan to continue to expand this project, and make others utilizing other languages and mediums to cocntinue increasing my understanding of SQL.

For this program the use is very straight-forward. I decided to utilize a terminal based program. The menu for using the program will print ever time we start the main loop, and then user input will be asked for. Given the choice input different actions will take place. I have the basics of adding, and updating entries into a database. Two tables are used to hold the students, and then classes that have been taken. At the start of every instance of this program it will delete the tables if they exist. This is just to show how it is done, and that the foreign keys update to allow this. Future renditions will have this removed and a delete function completed to allow for manual deletion of entries, and clearing out the whole table if nessissary.

The purpose behind writing and showing this program is to help provide an image of some of my skills. This was two weeks worth of research into what SQL is and how I can use python to code with it. I had no experience leading up to this point besides basic Python skills. I hope that this can become a bench mark to show my improvement and a stepping stone to allow me to build off of.

I have a short video demonstrating its use, and a basic walkthrough of how I coded this program here:

[Student Recoreds Demo Video](https://youtu.be/8CTXVIOd7oQ)

# Relational Database

I chose SQLite3 as my Database, this seemed to be a simple one that didn't involve getting other software but still utilized SQL code. 

I have two tables in use:
Students will hold the id for each student, along with first and last names, and an email.
Student_classes on the other hand holds a student ID foreign key and then class id and name of class along with the grade acheived.

Both don't have the most robust error checking at the moment but still suffice to allow for a basic add and display funciton for each. And then an inner join to show a snippet of both.

# Development Environment

I utilized Visual Studio Code to write this up. It had a couple extensions that work for python and git allowing me to slowly understand how to utilize a currsor and connection to work with the database in python.

The Python language and SQLite3 library I used are somewhat simple to use, whithout me having to udnerstand each little thing that happnes. This allowed me to go about learning the queries and different options I could use from different SQL tuturorial websites and then relativly easily get a rough version working in my own program.

# Useful Websites

A few of the websites I found most helpful in understanding how the code works.

- [SQLite Tutorial](https://www.sqlitetutorial.net)
- [Stack Overflow](https://stackoverflow.com)
- [W3Schools](https://www.w3schools.com)

# Future Work

Here a a few of the different additions I want to make as time goes on.

- Error checking and more security features to protect the database
- Delete options in menu and corresdponding functions
- More tables and learn/implement more joins with foreign keys.