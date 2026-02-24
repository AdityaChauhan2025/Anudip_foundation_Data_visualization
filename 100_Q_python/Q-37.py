# fibonacci_for
n = int(input().strip())

a, b = 0, 1
for _ in range(n):
    print(a)
    a, b = b, a + b