# sum_until_zero
total = 0

while True:
    num = int(input().strip())
    if num == 0:
        break
    total += num

print(total)