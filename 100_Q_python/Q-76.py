# student_topper
n = int(input("Enter number of students: ").strip())
marks = {}
for _ in range(n):
    name, score = input("Enter name and marks: ").split()
    marks[name] = int(score)

topper = max(marks, key=marks.get)
print("Topper:", topper)