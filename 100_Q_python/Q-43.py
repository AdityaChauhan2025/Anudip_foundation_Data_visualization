# palindrome_function
def is_palindrome(s):
    return s == s[::-1]

s = input().strip()

if is_palindrome(s):
    print("Palindrome")
else:
    print("Not Palindrome")