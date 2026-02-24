a = float(input().strip())
b = float(input().strip())
c = float(input().strip())

if a == b == c:
    print("Equilateral Triangle")
elif a == b or b == c or a == c:
    print("Isosceles Triangle")
else:
    print("Scalene Triangle")