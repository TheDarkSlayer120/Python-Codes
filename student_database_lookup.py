students_data = {
    "13467924": {"name": "John Wick", "course": "CIT", "year": "1"},
    "13681346": {"name": "Jane Doe", "course": "BIT", "year": "2"},
    "13467913": {"name": "Bob Robinson", "course": "Computer Science", "year": "3"},
}

search_id = input("Enter student ID to search: ")

if search_id in students_data:
    student = students_data[search_id]
    print("\nStudent Details:")
    print('-'*16)
    print(f"> Student ID: {search_id}")
    print(f"> Name: {student['name']}")
    print(f"> Course: {student['course']}")
    print(f"> Year: {student['year']}")
else:
    print("Student ID not recognised.")
