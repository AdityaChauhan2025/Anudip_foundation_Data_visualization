# merge_dictionaries
n1 = int(input("Enter number of elements in first dict: "))
dict1 = {}
for _ in range(n1):
    k, v = input().split()
    dict1[k] = int(v)

n2 = int(input("Enter number of elements in second dict: "))
dict2 = {}
for _ in range(n2):
    k, v = input().split()
    dict2[k] = int(v)

merged = dict1.copy()
merged.update(dict2)
print(merged)