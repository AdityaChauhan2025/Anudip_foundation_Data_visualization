# average_list
lst = list(map(int, input("Enter list elements separated by space: ").split()))
average = sum(lst) / len(lst) if lst else 0
print(average)