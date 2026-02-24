# rotate_list
lst = list(map(int, input("Enter list elements separated by space: ").split()))
k = int(input("Enter number of rotations: ").strip())
k = k % len(lst)
rotated = lst[k:] + lst[:k]
print(rotated)