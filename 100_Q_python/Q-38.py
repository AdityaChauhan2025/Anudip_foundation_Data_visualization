# reverse_string_for
s = input().strip()

rev = ""
for ch in s:
    rev = ch + rev

print(rev)