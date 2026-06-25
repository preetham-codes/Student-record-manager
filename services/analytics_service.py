def average_marks(students):
    if not students:
        print("No students in the list")
        return

    total = sum(s['Marks'] for s in students)
    avg = total / len(students)

    print(f"Average Marks: {avg:.2f}")


def max_marks(students):
    if not students:
        print("No students in the list")
        return

    topper = max(students, key=lambda x: x['Marks'])
    print("Topper Details:")
    print(topper)


def below_marks(students):
    found = False

    for student in students:
        if student['Marks'] < 40:
            print(student)
            found = True

    if not found:
        print("No students below 40")


def passing_percentage(students):
    if not students:
        print("No students in the list")
        return

    total = len(students)
    passed = sum(1 for s in students if s['Marks'] >= 40)

    percentage = (passed / total) * 100
    print(f"Passing Percentage: {percentage:.2f}%")