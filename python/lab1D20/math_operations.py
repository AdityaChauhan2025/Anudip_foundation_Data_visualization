# User-defined function to calculate addition and difference
def calculate(a, b):
    sum_result = a + b
    diff_result = a - b
    
    print("Addition =", sum_result)
    print("Difference =", diff_result)

# Function to calculate product
def product(a, b):
    return a * b

# Taking input from user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Function calls
calculate(num1, num2)
result = product(num1, num2)

# Output for product
print("Product =", result)