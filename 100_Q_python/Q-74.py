# set_subset
s1 = set(map(int, input("Enter first set elements: ").split()))
s2 = set(map(int, input("Enter second set elements: ").split()))
if s1 <= s2:
    print("Subset")
else:
    print("Not Subset")