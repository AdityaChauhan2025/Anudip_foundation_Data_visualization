# palindrome_check
s = input()
rev = ''
for c in s:
    rev = c + rev
print(s == rev)