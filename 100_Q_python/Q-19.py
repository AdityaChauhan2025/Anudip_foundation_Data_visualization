num = int(input().strip())
lower = int(input().strip())
upper = int(input().strip())

if lower <= num <= upper:
    print("Within Range")
else:
    print("Out of Range")