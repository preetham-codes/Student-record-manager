from services.student_service import *
from services.analytics_service import *

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
        print("Enter valid number")
        continue

    if choice == 1:
        add_student(students)
    elif choice == 2:
        view_student(students)
    elif choice == 3:
        search_student(students, int(input("Enter ID: ")))
    elif choice == 4:
        update_student(students, int(input("Enter ID: ")))
    elif choice == 5:
        delete_student(students, int(input("Enter ID: ")))
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
        print("Invalid choice")