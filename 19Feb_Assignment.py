#Assignment Name : Student Data Manager
#Description : Store data for 5 students using dictionaries, print topper, class average, and assign grades.
#Creating a list to store student data
students = []
#Collecting data for 5 students
for i in range(5):
    student = {}
    student['name'] = input(f"Enter name of student {i+1}: ")
    student['marks'] = float(input(f"Enter marks of student {i+1}: "))
    students.append(student)
#Finding the topper
topper = max(students, key=lambda x: x['marks'])
print(f"Topper: {topper['name']} with marks {topper['marks']}")
#Calculating class average
total_marks = sum(student['marks'] for student in students)
class_average = total_marks / len(students)
print(f"Class Average: {class_average}")
#Assigning grades based on marks
for student in students:
    if student['marks'] >= 90:
        student['grade'] = 'A'
    elif student['marks'] >= 80:
        student['grade'] = 'B'
    elif student['marks'] >= 70:
        student['grade'] = 'C'
    elif student['marks'] >= 60:
        student['grade'] = 'D'
    else:
        student['grade'] = 'F'
