# sort_dict_values
d = {}
n = int(input("Enter number of elements: "))
for _ in range(n):
    k, v = input().split()
    d[k] = int(v)

for k, v in sorted(d.items(), key=lambda item: item[1]):
    print(k, ":", v)