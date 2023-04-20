from grade import Grade
from teacher import Teacher

students = []

def AddStudent():
    while True:
        print()
        id = input('Enter Id: ')
        lastName = input('Enter Last Name: ')
        firstName = input('Enter First Name: ')
        middleName = input('Enter Middle Name: ')
        type = input('Enter Type: ')
        course = input('Enter Course: ')
        year = input('Enter Year: ')
        section = input('Enter Section: ')
        print('----------------------------')
        filipino = input('Grade Filipino: ')
        math = input('Grade Math: ')
        science = input('Grade Science: ')
        english = input('Grade English: ')

        stud = Grade(filipino, math, science, english)
        stud.id = id
        stud.last_name = lastName
        stud.first_name = firstName
        stud.middle_name = middleName
        stud.type = type
        stud.course = course
        stud.year = year
        stud.section = section

        students.append(stud)

        print()
        ans = input('Enter Another? [Y/N]: ')

        if (ans != 'Y'):
            break

    menu()

teacher = []

def AddTeacher():
    while True:
        print()
        id = input('Enter Id: ')
        lastName = input('Enter Your Last Name: ')
        firstName = input('Enter First Name: ')
        middleName = input('Enter Middle Name: ')
        type = input('Enter Type: ')
        department = input('Enter Your Department: ')
        position = input('Enter Your Position: ')

        teach = Teacher(department, position)
        teach.id = id
        teach.last_name = lastName
        teach.first_name = firstName
        teach.middle_name = middleName
        teach.type = type
        teach.department = department
        teach.position = position

        teacher.append(teach)

        print()
        ans = input('Enter Another? [Y/N]: ')

        if (ans != 'Y'):
            break

    menu()

def DeleteStudent():
    i = int(input('Enter Index: '))
    students.pop(i)

    menu()

def DeleteTeacher():
    i = int(input('Enter Index: '))
    teacher.pop(i)

    menu()

def DeleteAll():
    teacher.clear()
    students.clear()

    menu()

def SearchStudent():
    print()
    i = int(input('Enter Index: '))
    print('-------------------------------------------------------------------------------')
    print(f'{i} \t {students[i].getName()} \t | {students[i].getYrCourseSec()} \t | {students[i].getAverage()}')
    print('-------------------------------------------------------------------------------')

    menu()

def SearchTeacher():
    print()
    i = int(input('Enter Index: '))
    print('-------------------------------------------------------------------------------')
    print(f'{i} \t {teacher[i].getName()} \t | {teacher[i].getDepartment()} \t | {teacher[i].getPosition()}')
    print('-------------------------------------------------------------------------------')

    menu()

def DisplayStudent():
    print()
    print('-------------------------------------------------------------------------------')
    i = 0
    for s in students:
        print(f'{i} \t | {s.getName()} \t | {s.getYrCourseSec()} \t | {s.getAverage()}')
        i += 1
    print('-------------------------------------------------------------------------------')

    menu()

def DisplayTeacher():
    print()
    print('-------------------------------------------------------------------------------')
    i = 0
    for t in teacher:
        print(f'{i} \t | {t.getName()} \t | {t.getDepartment()} \t | {t.getPosition()}')
        i += 1
    print('-------------------------------------------------------------------------------')

    menu()

def DisplayAll():
    print()
    print('Student:')
    print('-------------------------------------------------------------------------------')
    i = 0
    for s in students:
        print(f'{i} \t | {s.getName()} \t | {s.getYrCourseSec()} \t | {s.getAverage()}')
        i += 1
    print('-------------------------------------------------------------------------------')
    print()
    print('Teacher:')
    print('-------------------------------------------------------------------------------')
    i = 0
    for t in teacher:
        print(f'{i} \t | {t.getName()} \t | {t.getDepartment()} \t | {t.getPosition()}')
        i += 1
    print('-------------------------------------------------------------------------------')

    menu()

def menu():
    print()
    print()
    print('::Menu::')
    print('D - Delete Student        S - Search Student ')
    print('A - Add Student            M - Display Student ')
    print('G - Delete Teacher       C - Search Teacher')
    print('F - Add Teacher          N - Display Teacher')
    print('X - Display All                 Z - Delete All')
    print()
    choice = input('Enter a Function: ')

    if (choice == 'D'):
        DeleteStudent()
    elif (choice == 'A'):
        AddStudent()
    elif (choice == 'S'):
        SearchStudent()
    elif (choice == 'M'):
        DisplayStudent()
    elif (choice == 'G'):
        DeleteTeacher()
    elif (choice == 'F'):
        AddTeacher()
    elif (choice == 'C'):
        SearchTeacher()
    elif (choice == 'N'):
        DisplayTeacher()
    elif (choice == 'X'):
        DisplayAll()
    elif (choice == 'Z'):
        DeleteAll()

    print()

menu()
