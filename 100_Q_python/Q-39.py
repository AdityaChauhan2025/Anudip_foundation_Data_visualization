# power_without_operator
base = int(input().strip())
exp = int(input().strip())

result = 1
for _ in range(exp):
    result *= base

print(result)