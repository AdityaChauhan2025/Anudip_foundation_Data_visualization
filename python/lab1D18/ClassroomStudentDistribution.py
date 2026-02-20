# Get data from the user
total_students = int(input("Enter the total number of students: "))
class_capacity = int(input("Enter the capacity of each class: "))

# Perform calculations
full_classes = total_students // class_capacity
remaining_students = total_students % class_capacity

# Display the results
print(f"\nResults:")
print(f"- Full classes: {full_classes}")
print(f"- Remaining students: {remaining_students}")
