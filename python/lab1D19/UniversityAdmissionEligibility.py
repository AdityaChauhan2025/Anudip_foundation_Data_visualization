print(" University Admission Eligibility Checker\n")

# Step 1: User Input
percentage_12th = float(input("Enter your 12th grade percentage: "))
studied_math = input("Did you study Mathematics? (yes/no): ").strip().lower()
entrance_score = float(input("Enter your entrance exam score: "))

# Step 2: Check eligibility
eligible = True
reasons = []

if percentage_12th < 75:
    eligible = False
    reasons.append(" 12th grade percentage less than 75%")

if studied_math != "yes":
    eligible = False
    reasons.append(" Mathematics not studied in 12th grade")

if entrance_score < 80:
    eligible = False
    reasons.append(" Entrance exam score less than 80")

# Step 3: Output result
print("\n" "\ Eligibility Result:")
if eligible:
    print(" Student is Eligible for Admission.")
else:
    print(" Student is NOT Eligible due to the following reason(s):")
    for reason in reasons:
        print(reason)
