def display_title():
    print('\n>Student Management System')
    print('--------------------------\n')
    print('Main menu:')
    print('----------\n')

def display_menu():
    print('1. Add a student')
    print('2. List students')
    print('3. Sort students')
    print('4. Clear the list')
    print('5. Exit')

def get_user_option():
    return int(input('Enter your choice (1-5): '))

def add_student(student_list):
    student_name = input('\nEnter student name: ')
    student_list.append(student_name)
    print(f'{student_name} added to the list.')

def list_students(student_list):
    if not student_list:
        print('\nThe list is empty.')
    else:
        print('\nList of students:')
        for student in student_list:
            print(student)

def sort_students(student_list):
    order = input('\nSort in ascending (A) or descending (D) order? ').upper()
    if order == 'A':
        student_list.sort()
    elif order == 'D':
        student_list.sort(reverse=True)
    else:
        print('Invalid option. No changes made.')

def clear_list(student_list):
    confirmation = input('\nAre you sure you want to clear the list? (yes/no): ').lower()
    if confirmation == 'yes':
        student_list.clear()
        print('List cleared.')
    else:
        print('List not cleared.')

def main():
    student_list = []

    while True:
        display_title()
        display_menu()

        choice = get_user_option()

        if choice == 1:
            add_student(student_list)
        elif choice == 2:
            list_students(student_list)
        elif choice == 3:
            sort_students(student_list)
        elif choice == 4:
            clear_list(student_list)
        elif choice == 5:
            print('Exiting the program.')
            break
        else:
            print('Invalid choice. Please enter a number between 1 and 5.')

if __name__ == '__main__':
    main()
