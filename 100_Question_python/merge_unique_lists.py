# merge_unique_lists
lst1 = list(map(int, input("Enter first list: ").split()))
lst2 = list(map(int, input("Enter second list: ").split()))
merged = list(dict.fromkeys(lst1 + lst2))
print(merged)