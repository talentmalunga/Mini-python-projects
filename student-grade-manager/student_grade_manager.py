class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def average(self):
        return sum(self.grades) / len(self.grades) if self.grades else 0

    def __str__(self):
        return f"{self.name} - Avg Grade: {self.average():.2f}"

def sort_students_by_average(students):
    return sorted(students, key=lambda s: s.average(), reverse=True)

def search_student(students, name):
    return next((s for s in students if s.name.lower() == name.lower()), None)

# Demo data
students = [Student("Harkim"),Student("Vuyolwethu"),Student("Talent")]

# sample grades
students[0].add_grade(85)
students[0].add_grade(90)

students[1].add_grade(70)
students[1].add_grade(75)

students[2].add_grade(95)
students[2].add_grade(100)

# Display all students
print("All Students:")
for s in students:
    print(s)

# Sort and display top performers
print("\nTop Performers:")
for s in sort_students_by_average(students):
   print(s)

# Search for a student
name = input("\nEnter student name to search: ")
result = search_student(students, name)
if result:
    print("Found:", result)
else:
    print("Student not found.")
