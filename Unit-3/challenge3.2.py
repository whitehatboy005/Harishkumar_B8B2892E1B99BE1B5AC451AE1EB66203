def sort_students(students):
    students.sort(key=lambda x: x.cgpa, reverse=True)
class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

# Create a list of student objects
students = [
    Student("John", "A001", 3.8),
    Student("Alice", "A002", 3.9),
    Student("Bob", "A003", 3.7),
    Student("Eve", "A004", 4.0)
]

# Sort the list of students based on CGPA
sort_students(students)

# Print the sorted list
for student in students:
    print("Name:", student.name)
    print("Roll Number:", student.roll_number)
    print("CGPA:", student.cgpa)
    print()
