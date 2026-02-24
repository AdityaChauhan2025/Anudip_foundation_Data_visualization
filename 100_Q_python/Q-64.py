# replace_negatives
lst = list(map(int, input("Enter list elements separated by space: ").split()))
lst = [x if x >= 0 else 0 for x in lst]
print(lst)