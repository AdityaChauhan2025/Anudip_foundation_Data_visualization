# char_frequency
s = input()
freq = {}
for c in s:
    freq[c] = freq.get(c, 0) + 1
for k, v in freq.items():
    print(f"{k}:{v}")