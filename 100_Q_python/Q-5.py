# compound_interest

p = float(input("Enter principal amount: "))
r = float(input("Enter rate of interest: "))
t = float(input("Enter time: "))

amount = p * (1 + r/100) ** t
ci = amount - p

print("Compound Interest:", ci)