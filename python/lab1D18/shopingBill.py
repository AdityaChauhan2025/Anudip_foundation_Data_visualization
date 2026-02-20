notebook_quantity = int(input("Enter the number of notebooks: "))
notebook_cost = float(input("Enter the cost per notebook: ₹"))

pen_quantity = int(input("Enter the number of pens: "))
pen_cost = float(input("Enter the cost per pen: ₹"))

# 1. Calculate the total bill amount
total_bill = (notebook_quantity * notebook_cost) + (pen_quantity * pen_cost)
print(f"\nTotal bill amount: ₹{total_bill:.2f}")

# 2. Calculate the remaining balance
cash_given = float(input("\nEnter the amount given by the customer: ₹"))
balance = cash_given - total_bill

if balance >= 0:
    print(f"Remaining balance: ₹{balance:.2f}")
else:
    print(f"Insufficient funds! The customer still owes: ₹{abs(balance):.2f}")
