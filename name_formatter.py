name = str(input("Enter your name > "))

name_capitalise = name.split()
if len(name_capitalise) == 2:
    first_name, second_name = name_capitalise
else:
    first_name = name
    second_name = ""
first_name = first_name.capitalize()
second_name = second_name.capitalize()

name_in_upper = name.upper()
name_in_lower = name.lower()

box_length = len(name) + 15

print("-" * box_length)
print("|", name_in_upper, "           |")
print("|     ", f"{first_name} {second_name}", "      |")
print("|          ", name_in_lower, " |")
print("-" * box_length)
