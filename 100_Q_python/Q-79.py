# sort_dict_keys
d = {}
n = int(input("Enter number of elements: "))
for _ in range(n):
    k, v = input().split()
    d[k] = int(v)

for k in sorted(d.keys()):
    print(k, ":", d[k])