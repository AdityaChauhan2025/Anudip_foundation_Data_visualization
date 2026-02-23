# attendance_tracker.py

def attendance_tracker(attendance):
    total_days = len(attendance)
    present_days = sum(attendance)

    # Calculate attendance percentage
    percentage = (present_days / total_days) * 100 if total_days > 0 else 0

    # Check if below 75%
    below_75 = percentage < 75

    # Replace consecutive absences (0,0) with warning flag "W"
    flagged_attendance = []
    i = 0
    while i < total_days:
        if i < total_days - 1 and attendance[i] == 0 and attendance[i + 1] == 0:
            flagged_attendance.append("W")  # Warning flag
            i += 2  # Skip next since it's consecutive
        else:
            flagged_attendance.append(attendance[i])
            i += 1

    # Display results
    print("\n----- Attendance Report -----")
    print("Total Days:", total_days)
    print("Present Days:", present_days)
    print("Attendance Percentage:", round(percentage, 2), "%")
    
    if below_75:
        print("Status: Below 75% (Short Attendance)")
    else:
        print("Status: Good Standing")

    print("Attendance with Warning Flags:", flagged_attendance)


# Take user input
user_input = input("Enter attendance (1 for Present, 0 for Absent) separated by spaces: ")

# Convert input into list of integers
attendance_list = list(map(int, user_input.split()))

# Run tracker
attendance_tracker(attendance_list)