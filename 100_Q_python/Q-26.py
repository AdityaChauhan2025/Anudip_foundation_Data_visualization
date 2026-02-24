# armstrong_check

num = int(input().strip())

temp = num
digits = len(str(num))
sum_of_powers = 0

while temp > 0:
    digit = temp % 10
    sum_of_powers += digit ** digits
    temp //= 10

if sum_of_powers == num:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")