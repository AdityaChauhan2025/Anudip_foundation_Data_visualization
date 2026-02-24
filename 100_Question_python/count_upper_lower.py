# count_upper_lower
s = input()
upper = sum(1 for c in s if c.isupper())
lower = sum(1 for c in s if c.islower())
print(f"Uppercase: {upper}, Lowercase: {lower}")