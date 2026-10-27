# Reflection Question 1:
# The first bug I found was a missing colon at the end of the for loop. I found it by reading the error message in the terminal which showed me the line with the problem and said that a colon was expected. This showed me that reading error messages can help me find where a problem is in my code.

# Reflection Question 2:
# The apply_discount function takes the price and tier and checks if the tier is gold, silver, bronze, or none of them. Then it applies the right discount to the price and returns the new discounted price.

# Reflection Question 3 / AI Disclosure:
# I used Chatgpt to help find the bugs in my code. AI helped me understand why the code was not working and how to get rid of the bugs.


# --- Exercise 1 ---
# Defining a function
def calculate_tax(price, rate):
    return price * rate

# Calling the function
tax1 = calculate_tax(100, 0.07)
tax2 = calculate_tax(250, 0.08)

print(f"Tax on $100 at 7%: ${tax1:.2f}")
print(f"Tax on $250 at 8%: ${tax2:.2f}")


# --- Exercise 2 ---

def apply_discount(price, tier):
    if tier == "gold":
        return price * 0.85
    elif tier == "silver":
        return price * 0.90
    elif tier == "bronze":
        return price * 0.95
    else:
        return price

# Calling the function with different tiers
original_price = 200

for tier in ["gold", "silver", "bronze", "none"]:
    print(f"{tier}: ${apply_discount(original_price, tier):.2f}")


# --- Exercise 3 ---

# Apply the gold discount to $200
discounted_price = apply_discount(200, "gold")
print(f"After gold discount: ${discounted_price:.2f}")

# Calculate 7% tax on the discounted price
tax = calculate_tax(discounted_price, 0.07)
after_tax = discounted_price + tax
print(f"After tax: ${after_tax:.2f}")

# Function that applies the discount and then adds tax
def final_price(price, tier, tax_rate):
    discounted_price = apply_discount(price, tier)
    tax = calculate_tax(discounted_price, tax_rate)
    return discounted_price + tax

print(f'final_price(200, "gold", 0.07) = ${final_price(200, "gold", 0.07):.2f}')

# --- Exercise 4 ---

orders = [(200, "gold"), (150, "silver"), (80, "bronze"), (500, "none")]

for price, tier in orders:
    total = final_price(price, tier, 0.07)
    print(f"Price: ${price} | Tier: {tier} | Final: ${total:.2f}")

 # --- Exercise 5 ---

sales = [120, 80, 250, 175, 90]

total = 0
for sale in sales:
    # Bug 3: This replaces the total with each sale instead of having to add each sale to the amount.
    total += sale
print(f"Total: ${total}")

count = 0
# Bug 1: The for loop is missing a colon at the end.
for sale in sales:
    count += 1
print(f"Count: {count}")

i = 0
# Bug 2: The loop lets i reach 5, but the last valid list index is 4.
while i < len(sales):
    print(sales[i])
    i += 1

# --- Exercise 6 ---

x = 100

def double_it():
    x = 999
    return x * 2

print(x)
print(double_it())
print(x)

# The x outside the function is a global variable. The x inside the function
# is a local variable, so changing it doesnt change the x outside the function.