# student_marks_analyzer.py

def analyze_marks(marks):
    # Remove invalid marks
    valid_marks = [m for m in marks if 0 <= m <= 100]

    if not valid_marks:
        print("No valid marks available.")
        return

    # Calculate average
    average = sum(valid_marks) / len(valid_marks)

    # Find topper(s)
    highest = max(valid_marks)
    toppers = [m for m in valid_marks if m == highest]

    # Assign grade based on average
    if average >= 90:
        grade = "A"
    elif average >= 75:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 50:
        grade = "D"
    else:
        grade = "F"

    # Display results
    print("\n----- Results -----")
    print("Valid Marks:", valid_marks)
    print("Average Marks:", round(average, 2))
    print("Highest Mark:", highest)
    print("Topper(s):", toppers)
    print("Overall Grade:", grade)


# Take user input
user_input = input("Enter student marks separated by spaces: ")

# Convert input string to list of integers
marks_list = list(map(int, user_input.split()))

# Analyze marks
analyze_marks(marks_list)