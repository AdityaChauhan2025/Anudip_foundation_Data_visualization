# first_non_repeating_char
s = input()
freq = {}
for c in s:
    freq[c] = freq.get(c, 0) + 1
for c in s:
    if freq[c] == 1:
        print(c)
        break