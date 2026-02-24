# unique_elements
def unique_list(lst):
    return list(set(lst))

n = int(input().strip())
lst = list(map(int, input().split()))

result = unique_list(lst)
print(*result)