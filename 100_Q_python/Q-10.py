# reverse_number

# Reverse a given number

# Read input
num = int(input().strip())

# Handle negative numbers
negative = False
if num < 0:
    negative = True
    num = -num

reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10

# Add negative sign back if needed
if negative:
    reverse = -reverse

# Print result
print(reverse)