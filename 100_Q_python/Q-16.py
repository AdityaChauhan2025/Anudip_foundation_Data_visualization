username = input().strip()
password = input().strip()

# Example validation
if username == "admin" and password == "1234":
    print("Login Successful")
else:
    print("Invalid Username or Password")