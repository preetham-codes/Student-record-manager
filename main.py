from services.student_service import add_student
from services.student_service import view_student
from services.student_service import search_student
from services.student_service import update_student
from services.student_service import delete_student
from services.student_service import extra_information

from services.analytics_service import average_marks
from services.analytics_service import max_marks
from services.analytics_service import below_marks
from services.analytics_service import passing_percentage



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