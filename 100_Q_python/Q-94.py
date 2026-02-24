# anagram_check
s1 = input().replace(' ', '').lower()
s2 = input().replace(' ', '').lower()
print(sorted(s1) == sorted(s2))