
numbers = tuple(map(int, input("Enter numbers separated by space: ").split()))
element = int(input("Enter element to count: "))

print("Tuple:", numbers)
print("Count:", numbers.count(element))