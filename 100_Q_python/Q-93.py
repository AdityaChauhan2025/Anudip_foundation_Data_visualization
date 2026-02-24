# replace_vowels
s = input()
vowels = 'aeiouAEIOU'
res = ''
for c in s:
    if c in vowels:
        res += '*'
    else:
        res += c
print(res)