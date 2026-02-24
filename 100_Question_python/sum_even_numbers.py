# sum_even_numbers
n = int(input().strip())

i = 1
total = 0

while i <= n:
    if i % 2 == 0:
        total += i
    i += 1

print(total)