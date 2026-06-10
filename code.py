n = int(input("Enter how many students: "))

students = []

for i in range(n):
    student = {
        "id": int(input("Enter ID: ")),
        "name": input("Enter name: "),
        "age": int(input("Enter age: ")),
        "course": input("Enter course: ")
    }

    students.append(student)

print("\nStudents details")

for student in students:
    print(f"ID: {student['id']}\n Name: {student['name']}\n Age: {student['age']}\n Course: {student['course']}\n")