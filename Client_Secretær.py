from Course import Course
from Lecture import Lecture
from Room import Room
from Student import Student
import csv
import getpass
def print_menu():
    print("--------------------------------")
    print(1, "Create an account")
    print(2, " Login to the system")
    print("--------------------------------")
print_menu()

def create_account():
    un=input("Enter your username")
    psw = getpass.getpass("Enter Your Password : ")
    data=[[un,psw]]
    file= open("Credentials.csv", "a", newline="")
    csvwriter = csv.writer(file)  #  create a csvwriter object
    csvwriter.writerows(data)  #  write  the data

def login():
    un = input("Enter your username")
    psw = getpass.getpass("Enter Your Password : ")
    fo = open("Credentials.csv", 'r')
    csvreader = csv.reader(fo)
    for row in csvreader:
        if row == [un, psw]:
            print("You are logged in")
            return True


def  client_secretær():
    print("-----------Creating 3  rooms---------------")
    # I have created the first room for you
    room1=Room("R1", "London", 30)
    room2=Room("R2", "Kurdistan", 35)
    room3=Room("R3", "Libnan", 40)



    print("-----------Creating 3  courses for these rooms-------------")
    # I have created the first course for you
    course1 = Course("D1", "Danish1", "Basic", room1)
    course2 = Course("D2", "Danish2", "Intermediate", room2)
    course3 = Course("D3", "Danish3", "Advanced", room3)




    print("----------------Creating 24 students------------------")
    # I have created the first student for you
    student1 = Student("Abubaker", 21, "abu@easj.dk")
    student2 = Student("Thomas", 25, "Thra@zealand.dk")
    student3 = Student("Firat", 23, "Firatkurt4000@hotmail.dk")
    student4 = Student("Bunyamin", 21, "Bunyamin@francofagismo.dk")
    student5 = Student("Walid", 40, "Waliddorshi@ged.dk")
    student6 = Student("peter", 22, "peter@zealand.dk")
    student7 = Student("Muhammed", 29, "muhammed@zealand.dk")
    student8 = Student("Hamudi", 18, "Hamudi@zealand.dk")
    student9 = Student("Kasper", 17, "kasper@zealand.dk")
    student10 = Student("Casper", 16, "Casper@zealand.dk")
    student11 = Student("Nassim", 14, "Nassim@zealand.dk")
    student12 = Student("Yasin,", 24, "yasin@zealand.dk")
    student13 = Student("Franco", 20, "franco@zealand.dk")
    student14 = Student("Jasmin", 14, "Jasmin@zealand.dk")
    student15 = Student("ole", 10, "ole@zealand.dk")
    student16 = Student("Ame", 11, "ame@zealand.dk")
    student17 = Student("Amo", 11, "Amo@zealand.dk")
    student18 = Student("benjamin", 9, "Benjamin@zealand.dk")
    student19 = Student("Kadir", 25, "Kadir@zealand.dk")
    student20 = Student("Dilara", 24, "Dilara@zealand.dk")
    student21 = Student("Mama", 29, "Mama@zealand.dk")
    student22 = Student("Hans", 11, "Hans@zealand.dk")
    student23 = Student("Isak", 2, "Isak@zealand.dk")
    student24 = Student("Sasia", 25, "Sasia@zealand.dk")
    student25 = Student("Emily", 23, "Emily@zealand.dk")

    print("-----------Creating 18 lectures--------------")
    # I have created the first lecture  for you
    lecture1 = Lecture("If statement", " 10:10", "13:45", "Tuesday")
    lecture2 = Lecture("If Statement2", " 10:10", "14:00", "Friday")
    lecture3 = Lecture("If Statement3", " 9:45", "13:45", "Monday")
    lecture4 = Lecture("Kommunikation", " 9:45", "13:45", "Monday")
    lecture5 = Lecture("Kommunikation2", " 9:45", "14:00", "Wensday")
    lecture6 = Lecture("Kommunikation3", " 9:45", "14:45", "Friday")
    lecture7 = Lecture("Orginasition", " 10:10", "13:45", "Tuesday")
    lecture8 = Lecture("Orginasition2", " 10:10", "15:45", "Satuday")
    lecture9 = Lecture("Orginasition3", " 12:45", "13:00", "Wensday")
    lecture10 = Lecture("Systemudvikling", " 10:10", "14:45", "Monday")
    lecture11 = Lecture("Systemudvikling2", " 9:45", "17:15", "Tuesday")
    lecture12 = Lecture("Systemudvikling3", " 8:45", "19:45", "Friday")
    lecture13 = Lecture("Pycharm", "7:00", "10:45", "Monday")
    lecture14 = Lecture("Pycharm2", "8:00", "11:45", "Tuesday")
    lecture15 = Lecture("Pycharm3", "9:00", "12:45", "Wensday")
    lecture16 = Lecture("Erhversøkonomi", "9:10", "16:45", "Monday")
    lecture17 = Lecture("Erhversøkonomi2", "9:45", "17:00", "Tuesday")
    lecture18 = Lecture("Erhversøkonomi3", "14:45", "19:45", "Wensday")

    print("-------------Assigning 8 students to each of the 3 course---------------")
    #implemenet the assign_student() function in the course class
    # then call it from here to assign a student (Alle studerende er blevet givet en Course)
    course1.assign_student(student24)
    course1.assign_student(student25)
    course1.assign_student(student23)
    course1.assign_student(student22)
    course1.assign_student(student21)
    course1.assign_student(student20)
    course1.assign_student(student19)
    course1.assign_student(student18)

    course2.assign_student(student17)
    course2.assign_student(student16)
    course2.assign_student(student15)
    course2.assign_student(student14)
    course2.assign_student(student13)
    course2.assign_student(student12)
    course2.assign_student(student11)
    course2.assign_student(student10)

    course3.assign_student(student9)
    course3.assign_student(student8)
    course3.assign_student(student7)
    course3.assign_student(student6)
    course3.assign_student(student5)
    course3.assign_student(student4)
    course3.assign_student(student3)
    course3.assign_student(student2)


    print("--------------Assigning 6 lectures to each course----------------")
    # implemenet the assign_lecture() function in the course class
    # then call it from here to assign a lecture (Alle Lectures er blevet givet courses)
    course1.assign_lecture(lecture1)
    course1.assign_lecture(lecture2)
    course1.assign_lecture(lecture3)
    course1.assign_lecture(lecture4)
    course1.assign_lecture(lecture5)
    course1.assign_lecture(lecture6)

    course2.assign_lecture(lecture7)
    course2.assign_lecture(lecture8)
    course2.assign_lecture(lecture9)
    course2.assign_lecture(lecture10)
    course2.assign_lecture(lecture11)
    course2.assign_lecture(lecture12)

    course3.assign_lecture(lecture13)
    course3.assign_lecture(lecture14)
    course3.assign_lecture(lecture15)
    course3.assign_lecture(lecture16)
    course3.assign_lecture(lecture17)
    course3.assign_lecture(lecture18)


    print("-------------Displaying students in each course-------------------")
    # implemenet the get_all_students() function in the course class
    # then call it from here to display all students in a specific course
    # HINT : to display all students , we use a for loop
    print("The student in Course 1")
    Liste1=course1.get_all_students()
    for elev in Liste1:
        print("\n")
        print(f"The student {elev.name} is in course 1")

    print("The student in course 2")
    Liste2 = course2.get_all_students()
    for elev in Liste2:
        print("\n")
        print(f"The student {elev.name} is in course 2")

    print("The student in course 3")
    Liste3 = course3.get_all_students()
    for elev in Liste3:
        print("\n")
        print(f"The student {elev.name} is in course 3")

    print("-------------Displaying lectures in each course-------------------")
    # implemenet the get_all_lectures() function in the course class
    # then call it from here to display all lectures in a specific course
    # HINT : to display all lectures , we use a for loop
    print("The lecture in course 1 ")
    Liste4 = course1.get_all_lectures()
    for lecture in Liste4:
        print("\n")
        print(f"The Lectures in course 1: from {lecture.day} {lecture._from} to {lecture._to}")

    print("The lecture in course 2")
    Liste5 = course2.get_all_lectures()
    for lecture in Liste5:
        print("\n")
        print(f"The Lectures in course 2: from {lecture.day} {lecture._from} to {lecture._to}")

    print("The Lecture in course 3")
    Liste6 = course3.get_all_lectures()
    for lecture in Liste6:
        print("\n")
        print(f"The Lectures in course 3: from {lecture.day} {lecture._from} to {lecture._to}")



    print("-------------Remove a student from her/his course-------------------")
    # implemenet the remove_student() function in the course class
    # then call it from here to remove the student you want to remove
    course1.remove_student(student24.email)
    Liste1 = course1.get_all_students()
    for elev in Liste1:
        print(f"The students in course 1: {elev.name}")

    print("-------------Remove a lecture from a course-------------------")
    # implemenet the remove_lecture() function in the course class
    # then call it from here to remove the lecture you want to remove
    course2.remove_lecture(lecture11.lecture_id)
    Liste5 = course2.get_all_lectures()
    for lecture in Liste5:
        print("\n")
        print(f"The lectures in Course 2: from {lecture.day} {lecture._from} to {lecture._to}")



while True:
    option=input("Please choose options 1 for new user and 2 for registered users>>")
    if(option=="1"):
       create_account()
    elif(option=="2"):
        status=login()
        if status==True:
           # we call the client_secretær() function
           client_secretær()
           break
