print(" Loan Approval System\n")

# Step 1: User Input
credit_score = int(input("Enter your credit score: "))
monthly_income = float(input("Enter your monthly income (₹): "))
existing_loan = float(input("Enter your existing loan amount (₹): "))

# Step 2: Check eligibility
approved = False
reasons = []

if credit_score < 600:
    reasons.append(" Credit score below 600")
elif 600 <= credit_score < 750:
    # Further check income and existing loans
    if monthly_income < 30000 and existing_loan > 500000:
        reasons.append(" Income less than ₹30,000 and existing loans exceed ₹5,00,000")
    else:
        approved = True
elif credit_score >= 750:
    approved = True

# Step 3: Output result
print("\n Loan Approval Result:")
if approved:
    print(" Loan Approved")
else:
    print(" Loan Rejected due to the following reason(s):")
    for reason in reasons:
        print(reason)
