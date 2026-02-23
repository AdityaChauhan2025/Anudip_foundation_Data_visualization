print(" Smart Login System – User Setup\n")

# Step 1: User sets their own username and password
username_set = input("Set your username: ").strip()
password_set = input("Set your password: ").strip()

print("\n Account created successfully!\n")

# Step 2: Login process
max_attempts = 3
attempt = 0
locked = False

while attempt < max_attempts:
    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()
    
    if username == username_set and password == password_set:
        print(" Login Successful! Welcome!")
        break
    else:
        attempt += 1
        print(f" Invalid credentials. Attempt {attempt} of {max_attempts}.\n")
        if attempt == max_attempts:
            locked = True
            print(" Account Locked due to 3 failed login attempts.")
