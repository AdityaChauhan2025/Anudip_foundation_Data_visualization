basic_salary = float(input("Enter the Basic salary (e.g., 25000): "))
bonus = float(input("Enter the Bonus amount (e.g., 5000): "))

# 2. Calculate HRA (20% of basic)
hra_percentage = 20
hra = basic_salary * (hra_percentage / 100)

# 3. Calculate total monthly salary
total_salary = basic_salary + hra + bonus

# 4. Display the results
print("-" * 30)
print(f"Calculated HRA: ₹{hra:,.2f}")
print(f"Total Monthly Salary: ₹{total_salary:,.2f}")

