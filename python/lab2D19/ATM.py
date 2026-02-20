print(" ATM Withdrawal System\n")

# Step 1: User Input
account_balance = float(input("Enter your account balance (₹): "))
daily_withdrawn = float(input("Enter total withdrawn today (₹): "))
atm_cash_available = float(input("Enter ATM cash available (₹): "))
withdraw_amount = float(input("Enter amount to withdraw (₹): "))

# Step 2: Check conditions
if withdraw_amount > account_balance:
    print(" Withdrawal failed: Insufficient account balance.")
elif daily_withdrawn + withdraw_amount > 50000:
    print(" Withdrawal failed: Exceeds daily withdrawal limit of ₹50,000.")
elif withdraw_amount > atm_cash_available:
    print(" Withdrawal failed: ATM does not have enough cash.")
else:
    # Withdrawal successful
    account_balance -= withdraw_amount
    daily_withdrawn += withdraw_amount
    atm_cash_available -= withdraw_amount
    print(f" Withdrawal successful! Amount withdrawn: ₹{withdraw_amount:.2f}")
    print(f"Remaining account balance: ₹{account_balance:.2f}")
    print(f"ATM cash remaining: ₹{atm_cash_available:.2f}")
