# factorial_while
n = int(input().strip())

fact = 1
i = 1
while i <= n:
    fact *= i
    i += 1

print(fact)