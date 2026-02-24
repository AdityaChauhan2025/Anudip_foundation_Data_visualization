# check_key_exists
n = int(input())
d = {}
for _ in range(n):
    k, v = input().split()
    d[k] = v
key_to_check = input()
print(key_to_check in d)