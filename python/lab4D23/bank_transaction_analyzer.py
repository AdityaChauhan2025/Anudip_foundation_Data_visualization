# bank_transaction_analyzer.py

def analyze_transactions(transactions):
    total_balance = sum(transactions)

    withdrawals = [t for t in transactions if t < 0]
    largest_withdrawal = min(withdrawals) if withdrawals else 0

    large_deposits = len([t for t in transactions if t > 10000])

    print("\nTotal Balance: ₹", total_balance)
    print("Largest Withdrawal: ₹", largest_withdrawal)
    print("Deposits > ₹10000:", large_deposits)


transactions_input = list(map(float, input("Enter transactions: ").split()))
analyze_transactions(transactions_input)
