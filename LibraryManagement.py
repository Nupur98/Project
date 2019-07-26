import time
from Functions import *
from IPython.display import clear_output
import sys
import getpass
print("----------------------------------------------------------------------------------------------")
print("Welcome To Library!\n\n")
print("1.Student")
print("2.Faculty")
print("3.Administrator\n")
ch=input("Select User: ")
print("----------------------------------------------------------------------------------------------")
clear_output()
if ch=='1':
    while True:
        clear_output()
        print("Welcome to the Student Panel!\n")
        print("Select the operation: \n")
        print("1.Print Student details")
        print("2.Print Book Details")
        print("#. Exit")
        choose=input()
        clear_output()
        if choose=='1':
            printStudentDetails()
        elif choose=='2':
            printBookDetails()
        elif choose=='#':
                sys.exit()
        else:
            print("Invalid Choice!!! Try Again.")
        time.sleep(8)
elif ch=='2':
     while True:
        clear_output()
        print("Welcome to the Faculty Panel!\n")
        print("Select the operation: \n")
        print("1.Print Faculty details")
        print("2.Print Book Details")
        print("#. Exit")
        choose=input()
        clear_output()
        if choose=='1':
            printFacultyDetails()
        elif choose=='2':
            printBookDetails()
        elif choose=='#':
                sys.exit()
        else:
            print("Invalid Choice!!! Try Again.")
        time.sleep(8)
elif ch=='3':
    clear_output()
    print("Enter password: ")
    s="asd456"
    password=getpass.getpass()
    if password==s:
        while True:
            clear_output()
            print("--------------------------------------------------------------------------------------------")
            print("1.Add a Student to Library")
            print("2.Add a Faculty to Library")
            print("3.Add a Book to Library")
            print("4.Issue Book to Student")
            print("5.Issue Book to Faculty")
            print("6.Return Book by Student")
            print("7.Return Book by Faculty")
            print("8.Search Student Records")
            print("9.Search Faculty Records")
            print("10.Search Book Records")
            print("11.Print all Student detils")
            print("12.Print all Faculty detils")
            print("13.Print all Book detils")
            print("#. Exit")
            print("---------------------------------------------------------------------------------------------")
            choose=input()
            clear_output()
            if choose=='1':
                addStudent()
            elif choose=='2':
                addFaculty()
            elif choose=='3':
                addBook()
            elif choose=='4':
                issue_book_to_student()
            elif choose=='5':
                issue_book_to_faculty()
            elif choose=='6':
                returnBookStudent()
            elif choose=='7':
                returnBookFaculty()
            elif choose=='8':
                printStudentDetails()
            elif choose=='9':
                printFacultyDetails()
            elif choose=='10':
                printBookDetails()
            elif choose=='11':
                showStudent()
            elif choose=='12':
                showFaculty()
            elif choose=='13':
                showBook()
            elif choose=='#':
                sys.exit()
            else:
                print("Invalid Choice!!!")
            time.sleep(8)
    else:
        clear_output()
        print("Incorrect Password!!! Try Again.")
        time.sleep(8)
else:
    print("Invalid Choice!!!")
    