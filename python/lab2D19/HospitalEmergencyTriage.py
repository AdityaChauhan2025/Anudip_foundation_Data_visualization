print(" Hospital Emergency Triage System\n")

# Step 1: User Input
age = int(input("Enter patient's age: "))
heart_rate = int(input("Enter patient's heart rate (bpm): "))
severe_injury = input("Does the patient have a severe injury? (yes/no): ").strip().lower()
condition = input("Current condition (normal/moderate): ").strip().lower()

# Step 2: Determine category
if heart_rate < 50 or heart_rate > 120 or severe_injury == "yes":
    category = "Critical"
elif condition == "moderate":
    category = "Moderate"
else:
    category = "Normal"

# Step 3: Upgrade priority if patient is senior
if age > 65 and category == "Moderate":
    category = "High Priority (upgraded from Moderate)"

# Step 4: Output result
print("\n Triage Result:")
print(f"- Patient Age: {age}")
print(f"- Heart Rate: {heart_rate} bpm")
print(f"- Severe Injury: {severe_injury.capitalize()}")
print(f"- Condition: {condition.capitalize()}")
print(f" Emergency Category: {category}")
