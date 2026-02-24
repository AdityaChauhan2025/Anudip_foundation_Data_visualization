# remove_duplicates
lst = list(map(int, input("Enter list elements separated by space: ").split()))
unique_lst = list(dict.fromkeys(lst))
print(unique_lst)