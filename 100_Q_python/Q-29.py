# gcd_while
a = int(input().strip())
b = int(input().strip())

while b != 0:
    a, b = b, a % b

print(a)