# frequency_list
lst = list(map(int, input("Enter list elements separated by space: ").split()))
freq = {}
for item in lst:
    freq[item] = freq.get(item, 0) + 1
for k, v in freq.items():
    print(k, ":", v)