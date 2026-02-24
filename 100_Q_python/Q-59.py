# even_odd_list
lst = list(map(int, input("Enter list elements separated by space: ").split()))
even = [x for x in lst if x % 2 == 0]
odd = [x for x in lst if x % 2 != 0]
print("Even:", even)
print("Odd:", odd)