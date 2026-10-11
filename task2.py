# Student ID Card Generator

name = input("Student name: ")
student_id = input("Student ID: ")
department = input("Department: ")
year = int(input("Year: "))          # stored as an integer
university = input("University: ")
phone = input("Phone number: ")      # stored as text so the leading 0 is kept

title = f"{university.upper()} STUDENT CARD"
lines = [
    f"Name: {name}",
    f"ID: {student_id}",
    f"Department: {department}",
    f"Year: {year}",
    f"University: {university}",
    f"Phone: {phone}",
]

width = max(len(title), *(len(line) for line in lines))
border = "+" + "-" * (width + 2) + "+"

print()
print(border)
print("| " + title.center(width) + " |")
print(border)
for line in lines:
    print("| " + line.ljust(width) + " |")
print(border)