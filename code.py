def extra_information(student):
    marks = student['Marks']

    # Result
    if marks < 40:
        student['Result'] = "Fail"
    else:
        student['Result'] = "Pass"

    # Grade
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


def print_profile(student):
    print(f"\nId: {student['Id']}")
    print(f"Name: {student['Name']}")
    print(f"Age: {student['Age']}")
    print(f"Course: {student['Course']}")
    print(f"Marks: {student['Marks']}")
    print(f"Result: {student['Result']}")
    print(f"Grade: {student['Grade']}\n")


def add_student(students):
    student = {
        "Id": int(input("Enter ID: ")),
        "Name": input("Enter Name: "),
        "Age": int(input("Enter Age: ")),
        "Course": input("Enter Course: "),
        "Marks": int(input("Enter marks (0-100): "))
    }

    
    for s in students:
        if s["Id"] == student["Id"]:
            print("ID already exists. Try again.")
            student["Id"] = int(input("Enter Id again"))
            return

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


def average_marks(students):
    if not students:
        print("No students in the list")
        return

    total = sum(student['Marks'] for student in students)
    avg = total / len(students)

    print(f"Average Marks: {avg:.2f}")


def max_marks(students):
    if not students:
        print("No students in the list")
        return

    topper = max(students, key=lambda x: x['Marks'])
    print("Topper Details:")
    print_profile(topper)


def below_marks(students):
    if not students:
        print("No students in the list")
        return

    found = False
    for student in students:
        if student['Marks'] < 40:
            print_profile(student)
            found = True

    if not found:
        print("No students below 40")


def passing_percentage(students):
    if not students: 
        print("No students in the list")
    return None 
    above = 0
    for student in students:
         if(student['Marks'] >= 40):
             above += 1 
             total_students = len(students)
             passing = (above / total_students) * 100
             print(f"Passing_percentage : {passing}")


# ---------------- MAIN PROGRAM ---------------- #

students = []

while True:
    print("""
Menu
1. Add Student
2. View Students
3. Search Student
4. Update Student
5. Delete Student
6. Average Marks
7. Topper
8. Below 40
9. Passing Percentage
10. Exit
""")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Enter a valid number")
        continue

    if choice == 1:
        add_student(students)

    elif choice == 2:
        view_student(students)

    elif choice == 3:
        search_id = int(input("Enter ID: "))
        search_student(students, search_id)

    elif choice == 4:
        search_id = int(input("Enter ID: "))
        update_student(students, search_id)

    elif choice == 5:
        search_id = int(input("Enter ID: "))
        delete_student(students, search_id)

    elif choice == 6:
        average_marks(students)

    elif choice == 7:
        max_marks(students)

    elif choice == 8:
        below_marks(students)

    elif choice == 9:
        passing_percentage(students)

    elif choice == 10:
        print("Thank you!")
        break

    else:
        print("Invalid choice. Try again.")