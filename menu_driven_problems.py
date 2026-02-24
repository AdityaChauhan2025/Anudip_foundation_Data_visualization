
def problem1_reverse_number():
    num = int(input("Enter a number: "))
    negative = num < 0
    if negative:
        num = -num
    rev = 0
    while num > 0:
        rev = rev * 10 + num % 10
        num //= 10
    print("Reversed number:", -rev if negative else rev)

def problem2_leap_year():
    year = int(input("Enter year: "))
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("Leap Year")
    else:
        print("Not a Leap Year")

def problem3_assign_grade():
    marks = float(input("Enter marks: "))
    if marks >= 90:
        print("Grade A")
    elif marks >= 75:
        print("Grade B")
    elif marks >= 50:
        print("Grade C")
    elif marks >= 35:
        print("Grade D")
    else:
        print("Fail")

def problem4_vowel_or_consonant():
    ch = input("Enter a character: ").lower()
    if ch in 'aeiou':
        print("Vowel")
    elif ch.isalpha():
        print("Consonant")
    else:
        print("Special character")

def problem5_digit_or_alphabet():
    ch = input("Enter a character: ")
    if ch.isdigit():
        print("Digit")
    elif ch.isalpha():
        print("Alphabet")
    else:
        print("Special character")

def problem6_divisible_by_3_5():
    num = int(input("Enter a number: "))
    if num % 3 == 0 and num % 5 == 0:
        print("Divisible by both 3 and 5")
    else:
        print("Not divisible by both 3 and 5")

def problem7_validate_login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username == "admin" and password == "1234":
        print("Login Successful")
    else:
        print("Invalid Username or Password")

def problem8_triangle_type():
    a = float(input("Enter side a: "))
    b = float(input("Enter side b: "))
    c = float(input("Enter side c: "))
    if a == b == c:
        print("Equilateral Triangle")
    elif a == b or b == c or a == c:
        print("Isosceles Triangle")
    else:
        print("Scalene Triangle")

def problem9_bmi_category():
    weight = float(input("Enter weight (kg): "))
    height = float(input("Enter height (m): "))
    bmi = weight / (height ** 2)
    if bmi < 18.5:
        print("Underweight")
    elif bmi < 25:
        print("Normal weight")
    elif bmi < 30:
        print("Overweight")
    else:
        print("Obese")

def problem10_number_in_range():
    num = int(input("Enter number: "))
    lower = int(input("Enter lower bound: "))
    upper = int(input("Enter upper bound: "))
    if lower <= num <= upper:
        print("Within Range")
    else:
        print("Out of Range")

def problem11_greatest_of_four():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    c = float(input("Enter third number: "))
    d = float(input("Enter fourth number: "))
    print("Greatest number is:", max(a, b, c, d))

def problem21_numbers_while():
    n = int(input("Enter N: "))
    i = 1
    while i <= n:
        print(i)
        i += 1

def problem22_factorial_while():
    n = int(input("Enter N: "))
    fact = 1
    i = 1
    while i <= n:
        fact *= i
        i += 1
    print("Factorial:", fact)

def problem23_reverse_number_while():
    num = int(input("Enter number: "))
    rev = 0
    while num > 0:
        rev = rev * 10 + num % 10
        num //= 10
    print("Reversed number:", rev)

def problem24_count_digits():
    num = int(input("Enter number: "))
    count = 0 if num != 0 else 1
    temp = num
    while temp != 0:
        count += 1
        temp //= 10
    print("Number of digits:", count)

def problem25_sum_even_numbers():
    n = int(input("Enter N: "))
    total = 0
    i = 1
    while i <= n:
        if i % 2 == 0:
            total += i
        i += 1
    print("Sum of even numbers:", total)

def problem26_armstrong_number():
    num = int(input("Enter number: "))
    temp = num
    digits = len(str(num))
    sum_of_powers = 0
    while temp > 0:
        sum_of_powers += (temp % 10) ** digits
        temp //= 10
    if sum_of_powers == num:
        print("Armstrong Number")
    else:
        print("Not an Armstrong Number")

def problem27_fibonacci_while():
    n = int(input("Enter N: "))
    a, b = 0, 1
    count = 0
    while count < n:
        print(a)
        a, b = b, a + b
        count += 1

def problem28_multiplication_table():
    num = int(input("Enter number: "))
    i = 1
    while i <= 10:
        print(f"{num} x {i} = {num*i}")
        i += 1

def problem29_gcd_while():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    while b != 0:
        a, b = b, a % b
    print("GCD:", a)

def problem30_sum_until_zero():
    total = 0
    while True:
        num = int(input("Enter number (0 to stop): "))
        if num == 0:
            break
        total += num
    print("Sum:", total)

# ------------------------ MENU ------------------------

def menu():
    print("\n--- Large Python Program (Problems 1–80) ---")
    print("Select problem number to execute:")
    print("1: Reverse number")
    print("2: Leap Year")
    print("3: Assign Grade")
    print("4: Vowel or Consonant")
    print("5: Digit or Alphabet")
    print("6: Divisible by 3 and 5")
    print("7: Validate Login")
    print("8: Triangle Type")
    print("9: BMI Category")
    print("10: Number in Range")
    print("11: Greatest of Four Numbers")
    print("21: Numbers 1 to N (while)")
    print("22: Factorial (while)")
    print("23: Reverse Number (while)")
    print("24: Count Digits")
    print("25: Sum of Even Numbers")
    print("26: Armstrong Number")
    print("27: Fibonacci (while)")
    print("28: Multiplication Table")
    print("29: GCD (while)")
    print("30: Sum until 0")
    print("0: Exit")

def run():
    while True:
        menu()
        choice = int(input("Enter problem number: "))
        if choice == 0:
            print("Exiting program...")
            break
        elif choice == 1:
            problem1_reverse_number()
        elif choice == 2:
            problem2_leap_year()
        elif choice == 3:
            problem3_assign_grade()
        elif choice == 4:
            problem4_vowel_or_consonant()
        elif choice == 5:
            problem5_digit_or_alphabet()
        elif choice == 6:
            problem6_divisible_by_3_5()
        elif choice == 7:
            problem7_validate_login()
        elif choice == 8:
            problem8_triangle_type()
        elif choice == 9:
            problem9_bmi_category()
        elif choice == 10:
            problem10_number_in_range()
        elif choice == 11:
            problem11_greatest_of_four()
        elif choice == 21:
            problem21_numbers_while()
        elif choice == 22:
            problem22_factorial_while()
        elif choice == 23:
            problem23_reverse_number_while()
        elif choice == 24:
            problem24_count_digits()
        elif choice == 25:
            problem25_sum_even_numbers()
        elif choice == 26:
            problem26_armstrong_number()
        elif choice == 27:
            problem27_fibonacci_while()
        elif choice == 28:
            problem28_multiplication_table()
        elif choice == 29:
            problem29_gcd_while()
        elif choice == 30:
            problem30_sum_until_zero()
        else:
            print("Problem not implemented yet or invalid choice.")

if __name__ == "__main__":
    run()