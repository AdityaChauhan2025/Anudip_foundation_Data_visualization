# gcd_function
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

a = int(input().strip())
b = int(input().strip())

print(gcd(a, b))