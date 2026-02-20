# Input values
transaction_amount = float(input("Enter transaction amount (₹): "))
account_age_months = int(input("Enter account age (in months): "))
is_international = input("Is the transaction international? (yes/no): ").strip().lower()

# Condition check
if (transaction_amount > 200000 and
    account_age_months < 6 and
    is_international == "yes"):
    
    print(" Transaction Flagged for Manual Verification.")
else:
    print(" Transaction is Normal.")
