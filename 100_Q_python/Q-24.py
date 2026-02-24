# count_digits
num = int(input().strip())

count = 0
if num == 0:
    count = 1
else:
    while num != 0:
        count += 1
        num //= 10

print(count)