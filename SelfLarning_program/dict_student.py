
name = input("Enter student name: ")
age = input("Enter age: ")
course = input("Enter course: ")

student = {
    "name": name,
    "age": age,
    "course": course
}

print("Student Details:")
for key, value in student.items():
    print(key, ":", value)