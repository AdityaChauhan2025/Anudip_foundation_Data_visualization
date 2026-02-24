# second_largest
lst = list(map(int, input("Enter list elements separated by space: ").split()))
unique_lst = list(set(lst))
unique_lst.sort()
print(unique_lst[-2])