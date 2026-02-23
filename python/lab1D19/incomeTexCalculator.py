print(" Human Mind Logic Training Program")

# Step 1: User input
income = float(input("Enter your annual income (₹): "))
age = int(input("Enter your age: "))
risk_taking = input("Do you like taking risks? (yes/no): ").strip().lower()

# Step 2: Determine thinking strategy
if age < 25:
    strategy = "exploratory thinking"
elif age <= 60:
    strategy = "practical thinking"
else:
    strategy = "wise & cautious thinking"

# Step 3: Use logic to calculate "tax" as a brain exercise
tax = 0
if age >= 60:
    exemption_limit = 300000
else:
    exemption_limit = 250000

if income <= exemption_limit:
    tax = 0
elif income <= 500000:
    tax = (income - exemption_limit) * 0.05
elif income <= 1000000:
    tax = ((500000 - exemption_limit) * 0.05) + ((income - 500000) * 0.20)
else:
    tax = ((500000 - exemption_limit) * 0.05) + (500000 * 0.20) + ((income - 1000000) * 0.30)

# Step 4: Mind-use advice
print("\n Mind Usage Analysis:")
print(f"- Based on your age, you tend to use {strategy}.")
print(f"- Risk-taking mindset: {risk_taking}")
print(f"- Logic exercise (simulated tax calculation) result: ₹{tax:.2f}")
print(" Tip: Keep practicing decision-making, calculation, and strategy thinking to sharpen your mind!")
