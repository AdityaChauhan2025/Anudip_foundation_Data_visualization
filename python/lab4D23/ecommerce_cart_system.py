# ecommerce_cart_system.py

def calculate_bill(prices):
    # Remove duplicate items
    unique_prices = list(set(prices))

    # Calculate total
    total = sum(unique_prices)
    print("Total after removing duplicates: ₹", total)

    # Apply 10% discount if total > 5000
    if total > 5000:
        discount = total * 0.10
        total -= discount
        print("Discount Applied (10%): ₹", round(discount, 2))
    else:
        print("No discount applied.")

    # Add GST 18%
    gst = total * 0.18
    final_amount = total + gst

    print("GST (18%): ₹", round(gst, 2))
    print("Final Payable Amount: ₹", round(final_amount, 2))


# Take user input
user_input = input("Enter product prices separated by spaces: ")

# Convert input to list of floats
price_list = list(map(float, user_input.split()))

# Calculate final bill
calculate_bill(price_list)
