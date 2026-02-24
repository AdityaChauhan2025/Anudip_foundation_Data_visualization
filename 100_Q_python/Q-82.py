# safe_remove_key
n = int(input())
d = {}
for _ in range(n):
    k, v = input().split()
    d[k] = v
key_to_remove = input()
d.pop(key_to_remove, None)
print(d)