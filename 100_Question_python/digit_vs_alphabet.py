ch = input().strip()

if ch.isdigit():
    print("Digit")
elif ch.isalpha():
    print("Alphabet")
else:
    print("Special Character")