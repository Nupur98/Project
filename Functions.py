from FacultyClass import *
from BookClass import *
from StudentClass import *
import pickle


#Function to search book
def searchBook(isbn):
    d={}
    with open("Book_dt.pkl","rb") as f:
        d=pickle.load(f)
        for i in d.keys():
            if isbn == i:
                return d
        else:
            return False
#Function to search book by title
def searchBookTitle(title):
    d={}
    with open("Book_dt.pkl","rb") as f:
        d=pickle.load(f)
        for i,y in d.items():
            if title.lower() == y.title.lower():
                print(f"Title: {y.title}\nAuthor: {y.author}\nNo of Copies: {y.no_of_copies}")
                break
        else:
            print("No book Found!!!")
#Function to search book by ISBN
def searchBookIsbn(isbn):
    with open("Book_dt.pkl","rb") as f:
        d=pickle.load(f)
        for i,y in d.items():
            if isbn == i:
                print(f"Title: {y.title}\nAuthor: {y.author}\nNo of Copies: {y.no_of_copies}")
                break
        else:
            print("No book Found!!!")
#Function to Search book by Author name.
def searchBookAuthor(author):
    d={}
    with open("Book_dt.pkl","rb") as f:
        d=pickle.load(f)
        for i,y in d.items():
            if author.lower() == y.author.lower():
                print(f"Title: {y.title}\nAuthor: {y.author}\nNo of Copies: {y.no_of_copies}")
                break
        else:
            print("No book Found!!!")
#Function to choose the search mode.
def printBookDetails():
    ch=input("Enter the choice for search mode:\n1->ISBN     2->Title     3->Author")
    if ch=='1':
        isbn=int(input("Enter the ISBN: "))
        searchBookIsbn(isbn)
    elif ch=='2':
        title=input("Enter the title: ")
        searchBookTitle(title)
    elif ch=='3':
        author=input("Enter the author: ")
        searchBookAuthor(author)
    else:
        print("Invalid Choice!!!")
#Function to add book to library
def addBook():
    title=input("Enter the book title: ")
    author=input("Enter the author: ")
    isbn=int(input("Enter ISBN: "))
    if isbn<1000000000000 or isbn >= 10000000000000:
        print("Invalid ISBN!!! Try Again!!!")
        return
    no_of_copies=int(input("Enter no of copies: "))
    d={}
    with open("Book_dt.pkl","rb") as f:
        d=pickle.load(f)
        for i in d.keys():
            if isbn == i:
                d[i].no_of_copies+=no_of_copies
                break
        else:
            d[isbn]=Book(title,author,no_of_copies)
    with open("Book_dt.pkl","wb") as f:
        pickle.dump(d,f)
        print("Book details entered successfully!!!")
#Function that search for a student and returns the object
def searchStudent(st_id):
    l=loadStudentList()
    for i in l:
        if i.st_roll ==st_id:
            return i
    else:
        return False
#Function to load student list
def loadStudentList():
    l=[]
    with open ("Student_dt.pkl",'rb') as f:
        l=pickle.load(f)
    return l
#Function to print details of all Students.
def showStudent():
    l=loadStudentList()
    for i in l:
        print("----------------------------------------------------------------------------------------")
        print(f"Name: {i.name}\nBranch: {i.branch}\nRoll no: {i.st_roll}\nNo of books issued: {i.no_of_books}\nList of books: {i.book_list}")
    if l==[]:
        print("No Student Entered!!!")
#Function to add Student to library.
def addStudent():
    name=input("Enter the name of Student: ")
    print("Select branch: ")
    print("1.Computer Science")
    print("2.Mechanical")
    print("3.Electrical")
    print("4.Civil")
    ch=input()
    if ch=='1':
        branch="CS"
    elif ch=="2":
        branch="ME"
    elif ch=='3':
        branch="EC"
    elif ch=='4':
        branch="CE"
    else:
        print("Invalid Choice!!!")
        return
    s_id=int(input("Enter Admission id: "))
    if s_id < 1000 or s_id > 9999:
        print("Invalid Student admission id!!! Try again")
        return
    std_roll="0187"+branch+repr(s_id)
    if searchStudent(s_id) != False:
        print("Student already present!!! Invalid data . Try again!!!")
        return
    l=loadStudentList()
    l.append(Student(name,branch,std_roll))
    with open("Student_dt.pkl","wb") as f:
        pickle.dump(l,f)
    print("Student details entered successfully!!!")
#Function to show book details.
def showBook():
    with open("Book_dt.pkl","rb") as f:
        d=pickle.load(f)
    for i,y in d.items():
            if y.no_of_copies > 0:
                print("-------------------------------------------------------------------------------------")
                print(f"ISBN: {i}\nTitle: {y.title}\nAuthor: {y.author}\nNo of Copies: {y.no_of_copies}")
    if d=={}:
        print("No Books Entered!!!")
#Function to print student detail.
def printStudentDetails():
    s_id=input("Enter student enrollment no: ")
    i=searchStudent(s_id)
    if i:
        print(f"Name: {i.name}\nBranch: {i.branch}\nRoll no: {i.st_roll}\nNo of books issued: {i.no_of_books}\nList of books: {i.book_list}")
    else:
        print("Invalid Enrollment no!!!")
        
#Function to issue book to student.
def issue_book_to_student():
    std_id=input("Enter the student enrollment no: ")
    i=searchStudent(std_id)
    if i==False:
        print('Student not found. Cannot Issue Book.')
        return
    if i.no_of_books >= 4:
        print('Student Has Reached Book Limit. Cannot Issue Book.')
        return
    book_id=int(input("Enter the ISBN no: "))
    a= searchBook(book_id)
    if a == False:
        print("Wrong Isbn!!!")
        return
    for x in i.book_list:
        if x==book_id:
            print("This book is already issued by you!!!")
            return
    if a[book_id].no_of_copies == 0 :
        print("Book not avaliable now!!!")
        return
    a[book_id].no_of_copies-=1
    with open("Book_dt.pkl","wb") as f:
        pickle.dump(a,f)
    z=loadStudentList()
    for w in z:
        if w.st_roll == std_id:
            w.no_of_books+=1
            w.book_list.append(book_id)
    with open("Student_dt.pkl","wb") as f:
        pickle.dump(z,f)
    print("Book Issued successfully!!!")
#Function to Return book from student
def returnBookStudent():
    sd_id=input("Enter the enrollment no: ")
    i=searchStudent(sd_id)
    if i == False:
        print(f'Student with {sd_id} not present. Cannot return book.')
        return
    b_isbn=int(input("Enter the ISBN: "))
    l=loadStudentList()
    for i in l:
        if (i.st_roll==sd_id) and (sd_id in i.book_list):
            i.book_list.remove(b_isbn)
            break
    else:
        print("Invalid Details. Try Again!!!")
        return
    with open("Student_dt.pkl","wb") as f:
        pickle.dump(l,f)
    b={}
    with open("Book_dt.pkl","rb") as f:
        b=pickle.load(f)
    b[b_isbn].no_of_copies+=1
    with open("Book_dt.pkl","wb") as f:
        pickle.dump(b,f)
    print("Book returned successfully!!!")
#Function to Search a faculty
def searchFaculty(f_id):        
    l=loadFacultyList()
    for i in l:
        if i.eid == f_id:
            return i
    else:
        return False
#Function to print details of all Faculties.
def showFaculty():
    l=loadFacultyList()
    for i in l:
        print("-------------------------------------------------------------------------------------")
        print(f"Name: {i.ename}\nFaculty Id no: {i.eid}\nList of books: ")
        for x,y in i.book_list.items():
            print(f"ISBN: {x}\tNo of Copies: {y}")
    if l==[]:
        print("No faculty Entered")
#Function to load Faculty list.
def loadFacultyList():
    l=[]
    with open ("Faculty_dt.pkl",'rb') as f:
        l=pickle.load(f)
    return l          
#Function to print detail of a faculty.
def printFacultyDetails():
    f_id=int(input("Enter Faculty Id no: "))
    i=searchFaculty(f_id)
    if i:
        print(f"Name: {i.ename}\nFaculty Id no: {i.eid}\nList of books: {i.book_list.items()}")
    else:
        print("Invalid Faculty Id no!!!")
#Function to add faculty.
def addFaculty():
    name=input("Enter the faculty name: ")
    eid=int(input("Enter the faulty id: "))
    n_book_issued=0
    if eid>99999 or eid<10000:
        print("Invalid Faculty Id. Try Again!!!")
        return
    if searchFaculty(eid)!=False:
        print("Faculty already Present!!! Invalid Data. Try Again!!!")
        return
    l=loadFacultyList()
    l.append(Faculty(name,eid,n_book_issued))
    with open("Faculty_dt.pkl","wb") as f:
        pickle.dump(l,f)
        print("Faculty details entered successfully!!!")
#Function to issue book to faculty.
def issue_book_to_faculty():
    ep_id=int(input("Enter the Faculty id: "))
    i=searchFaculty(ep_id)
    if i == False:
        print(f'Employee with {ep_id} not present. Cannot issue book.')
        return
    b_isbn=int(input("Enter the ISBN: "))
    no_of_copies=int(input("Enter the no of copies: "))
    b=searchBook(b_isbn)
    if (b == False) or (b[b_isbn].no_of_copies < no_of_copies):
        print(f'Book with {b_isbn} not available/Copies Exhausted. Cannot issue book')
        return
    l=loadFacultyList()
    for i in l:
        if i.eid==ep_id:
            i.book_list[b_isbn]+=no_of_copies
    with open("Faculty_dt.pkl","wb") as f:
        pickle.dump(l,f)
    b[b_isbn].no_of_copies-=no_of_copies
    with open("Book_dt.pkl","wb") as f:
        pickle.dump(b,f)
    print("Book issued successfully!!!")
#Function to return book from Faculty.
def returnBookFaculty():
    ep_id=int(input("Enter the Faculty id: "))
    i=searchFaculty(ep_id)
    if i == False:
        print(f'Employee with {ep_id} not present. Cannot return book.')
        return
    b_isbn=int(input("Enter the ISBN: "))
    no_of_copies=int(input("Enter the no of copies: "))
    l=loadFacultyList()
    for i in l:
        if i.eid==ep_id and i.book_list[b_isbn]>=no_of_copies:
            i.book_list[b_isbn]-=no_of_copies
            if i.book_list[b_isbn]==0:
                del i.book_list[b_isbn]
            break
    else:
        print("Invalid Details. Try Again!!!")
        return
    with open("Faculty_dt.pkl","wb") as f:
        pickle.dump(l,f)
    b={}
    with open("Book_dt.pkl","rb") as f:
        b=pickle.load(f)
    b[b_isbn].no_of_copies+=no_of_copies
    with open("Book_dt.pkl","wb") as f:
        pickle.dump(b,f)
    print("Book returned successfully!!!")