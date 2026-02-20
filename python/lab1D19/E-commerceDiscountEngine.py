print(" Human Brain E-commerce Discount Engine\n")

# Step 1: User Input
cart_value = float(input("Enter your cart value (₹): "))
membership = input("Enter your membership (Silver/Gold/Platinum): ").strip().lower()
festival = input("Is it festival season? (yes/no): ").strip().lower()

# Step 2: Brain logic – Determine possible discounts
discounts = []

# Membership discounts
if membership == "silver":
    discounts.append(0.05)  # 5%
elif membership == "gold":
    discounts.append(0.10)  # 10%
elif membership == "platinum":
    discounts.append(0.15)  # 15%

# Cart value discount
if cart_value >= 5000:
    discounts.append(0.05)  # 5% extra for big cart

# Festival season discount
if festival == "yes":
    discounts.append(0.10)  # 10% extra

# Step 3: Apply the highest eligible discount
if discounts:
    max_discount = max(discounts)
else:
    max_discount = 0

final_amount = cart_value * (1 - max_discount)

# Step 4: Print results
print("\n Brain Decision Output:")
print(f"- Cart Value: ₹{cart_value:.2f}")
print(f"- Membership: {membership.capitalize()}")
print(f"- Festival Season: {festival.capitalize()}")
print(f"- Highest Eligible Discount: {max_discount*100:.0f}%")
print(f" Final Payable Amount: ₹{final_amount:.2f}")
