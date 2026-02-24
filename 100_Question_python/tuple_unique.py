# tuple_unique
t = tuple(map(int, input("Enter tuple elements separated by space: ").split()))
if len(t) == len(set(t)):
    print("Unique")
else:
    print("Not Unique")