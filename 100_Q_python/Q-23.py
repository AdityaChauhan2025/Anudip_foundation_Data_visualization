# reverse_number_while
num = int(input().strip())

reverse = 0
while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10

print(reverse)