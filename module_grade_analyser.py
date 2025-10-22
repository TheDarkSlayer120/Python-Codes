while True:
    try:
        num_students = int(input('Enter the number of students: '))
        break
    except ValueError:
        print('Invalid. Please enter valid number of students')
print()

grades = []

for student in range(1, num_students + 1):
    while True:
        try:
            mark = int(input(f'Enter the mark {student}: '))
            break
        except ValueError:
            print('Invalid input. Please enter a valid mark.')

    grades.append(mark)

overall_marks = sum(grades)
average_mark = overall_marks // num_students
max_grade = max(grades)
min_grade = min(grades)

print()
print('Overall Module Statistics:')
print('-'*26)
print(f'Average mark: {average_mark}')
print(f'Maximum grade: {max_grade}')
print(f'Minimum grade: {min_grade}')
print()

grades.sort()

for grade in grades:
    result = "Pass" if grade >= 40 else "Fail"
    print(f"Student no. {grades.index(grade) + 1}    Marks: {grade},    Result: {result}")
