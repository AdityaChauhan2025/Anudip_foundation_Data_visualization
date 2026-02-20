print(" Electricity Bill Calculator\n")

# Step 1: User Input
units_consumed = float(input("Enter units of electricity consumed: "))
senior_citizen = input("Are you a senior citizen? (yes/no): ").strip().lower()

# Step 2: Calculate bill based on slabs
bill = 0

if units_consumed <= 100:
    bill = units_consumed * 5
elif units_consumed <= 300:
    # First 100 units @5/unit + remaining units @7/unit
    bill = (100 * 5) + ((units_consumed - 100) * 7)
else:
    # First 100 units @5/unit + next 200 units @7/unit + remaining @10/unit
    bill = (100 * 5) + (200 * 7) + ((units_consumed - 300) * 10)

# Step 3: Apply senior citizen discount
if senior_citizen == "yes":
    discount = bill * 0.10
    bill -= discount
    print(f"\n Senior citizen discount applied: ₹{discount:.2f}")

# Step 4: Display final bill
print(f" Total Electricity Bill: ₹{bill:.2f}")
