# common_elements_lists
lst1 = list(map(int, input("Enter first list: ").split()))
lst2 = list(map(int, input("Enter second list: ").split()))
common = list(set(lst1) & set(lst2))
print(common)