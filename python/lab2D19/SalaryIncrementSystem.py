print(" Salary Increment Calculator\n")

# Step 1: User Input
performance = int(input("Enter performance rating (1-5): "))
experience = float(input("Enter years of experience: "))
attendance = float(input("Enter attendance percentage: "))

# Step 2: Base increment based on performance
if performance == 5:
    increment = 20  # 20%
elif performance == 4:
    increment = 15
elif performance == 3:
    increment = 10
elif performance == 2:
    increment = 5
else:
    increment = 0

# Step 3: Bonus based on experience
if experience >= 10:
    increment += 5   # Extra 5% for very experienced employees
elif experience >= 5:
    increment += 2   # Extra 2% for mid-level experience

# Step 4: Attendance adjustment
if attendance < 75:
    print(" Low attendance: reducing increment by 5%")
    increment -= 5
    if increment < 0:
        increment = 0  # Minimum increment 0%

# Step 5: Output final increment
print(f"\n Final Salary Increment: {increment}%")
