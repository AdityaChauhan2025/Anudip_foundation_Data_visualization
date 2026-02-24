# list_palindrome
lst = list(map(int, input("Enter list elements separated by space: ").split()))
if lst == lst[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")