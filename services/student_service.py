from utils.display import print_profile
from models.student import create_student

def extra_information(student):
    marks = student['Marks']

    if marks < 40:
        student['Result'] = "Fail"
    else:
        student['Result'] = "Pass"

    if marks > 90:
        student['Grade'] = "A+"
    elif marks >= 75:
        student['Grade'] = "A"
    elif marks >= 60:
        student['Grade'] = "B"
    elif marks >= 40:
        student['Grade'] = "C"
    else:
        student['Grade'] = "F"


def add_student(students):
    id = int(input("Enter ID: "))
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    course = input("Enter Course: ")
    marks = int(input("Enter marks (0-100): "))

    for s in students:
        if s["Id"] == id:
            print("ID already exists.")
            return

    student = create_student(id, name, age, course, marks)
    extra_information(student)
    students.append(student)
    print("Student added successfully")


def view_student(students):
    if not students:
        print("No students found.")
        return

    for student in students:
        print_profile(student)


def search_student(students, search_id):
    for student in students:
        if student["Id"] == search_id:
            print_profile(student)
            return

    print("Student not found")


def update_student(students, search_id):
    for student in students:
        if student["Id"] == search_id:
            student["Name"] = input("Enter new Name: ")
            student["Age"] = int(input("Enter new Age: "))
            student["Course"] = input("Enter new Course: ")
            student["Marks"] = int(input("Enter new marks: "))

            extra_information(student)
            print("Student updated successfully")
            return

    print("Student not found")


def delete_student(students, search_id):
    for student in students:
        if student["Id"] == search_id:
            students.remove(student)
            print("Student deleted successfully")
            return

    print("Student not found")