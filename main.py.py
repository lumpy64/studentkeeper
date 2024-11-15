from sys import exec_prefix

student_record = {}
import _json as json
import json

def student_record_func():
    while True:
        try:
            student = input("enter the student's name:")
            print("")
            grade = int(input("enter their score:"))
            student_record[student] = grade
            print("The current database of students is:")
            print("")
            for student, grade in student_record.items():
                print("Student name: ",student, "  Grade: ", grade)
            print("")
            print("Please make another selection!")
            print("")
            main_menu()
        except:
            print("Please enter valid data!")
            print("")

def show_student_records():
    print("The current database of students is:")
    print("")
    for student, grade in student_record.items():
        print("Student name: ", student, "  Grade: ", grade)
    print("")
    print("Please make another selection!")
    print("")
    main_menu()

def student_average():
    try:
        totalmark = sum(student_record.values())
        average = (totalmark / len(student_record))
        print(f"The class average was: {average:.2f}")
        print("")
    except:
        print("Average Calculation Failed! Please try entering information into database!")
        print("")
    main_menu()

def savetofile():
    file = input("Please choose file name (please in .json format) to save current database to: ")
    print("now saving!")
    print("")
    try:
        with open(file, 'w') as file:
            file.write(json.dumps(student_record))
            print("Saved to file!")
    except:
        print("Error saving file!")
    print("")
    print("Please make another selection!")
    print("")
    main_menu()

def loadfromfile():
    global student_record
    print("")
    file = input("Please choose the file (in .json format) you would like to load from: ")
    try:
        with open(file, 'r') as file:
            student_record = json.load(file)
            print(".json loaded!")
    except:
        print("Error with file found, please check path and data!")
    print("")
    print("Please make another selection!")
    print("")
    main_menu()

def literaldictionary():
    print("As requested, this is the literal contents of the dictionary for debugging")
    print("")
    print(student_record)
    print("")
    print("Please make another selection!")
    main_menu()


def main_menu():
    print("1. Enter a new student record")
    print("")
    print("2. View current contents of the Student Database")
    print("")
    print("3. Calculate average grade percentage of Student Database")
    print("")
    print("4. Save current database to file")
    print("")
    print("5. Load database from file")
    print("")
    print("6. View the literal contents of the student record (for debugging)")
    print("")
    select = int(input("Please make your selection now: "))
    print("")
    try:
        if select == 1:
            student_record_func()
        elif select == 2:
            show_student_records()
        elif select == 3:
            student_average()
        elif select == 4:
            savetofile()
        elif select == 5:
            loadfromfile()
        elif select == 6:
            literaldictionary()
    except:
        print("Please make a valid selection as the number of your selection")

print("----Student Keeper 3001----")
print("Please make a selection!")
print("")
main_menu()






