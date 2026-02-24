# tuple_count
t = tuple(map(int, input("Enter tuple elements separated by space: ").split()))
element = int(input("Enter element to count: ").strip())
print(t.count(element))