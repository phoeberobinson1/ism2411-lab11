"""
Reflection
1. Use bracket notation when you expect the key to always be present and want 
your code to fail fast if it's missing (e.g., required database fields). Use 
.get() when dealing with optional data or user inputs where a missing key is 
normal and you want to supply a safe default fallback value.
2. This pattern is identical to a Pivot Table or a SUMIF function in Excel. 
The Python version is more useful for massive datasets because it processes 
rows automatically without dragging formulas down thousands of cells, scales 
effortlessly, and avoids memory or UI lag issues common in spreadsheets.
"""
#Exercise 1

customer = {
    "name": "Jordan Lee",
    "email": "jordan@example.com",
    "tier": "gold",
    "ytd_spend": 1250.50
}

print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])
print(customer)


#Exercise 2

customer["phone"] = "555-0198"
print("After adding phone:", customer)

customer["tier"] = "platinum"
print("After updating tier:", customer)

del customer["email"]
print("After deleting email:", customer)


#Exercise 3

email_result = customer.get("email", "no email on file")
print(f".get() result: {email_result}")

try:
    print(customer["email"])
except KeyError:
    print("Caught KeyError: 'email' key does not exist in dictionary.")


#Exercise 4

for key, value in customer.items():
    print(f"{key}: {value}")


#Exercise 5

tier_discounts = {
    "bronze": 0, 
    "silver": 0.05, 
    "gold": 0.10, 
    "platinum": 0.15
}

purchase_amount = 200.0
current_tier = customer["tier"]

discount_rate = tier_discounts.get(current_tier, 0)
final_price = purchase_amount * (1 - discount_rate)

print(f"Tier: {current_tier}")
print(f"Discount Rate: {discount_rate * 100}%")
print(f"Final Price: ${final_price:.2f}")


#Exercise 6

customers = [
    {"name": "Alice Smith", "tier": "bronze"},
    {"name": "Bob Jones", "tier": "silver"},
    {"name": "Charlie Brown", "tier": "gold"},
    {"name": "Diana Prince", "tier": "platinum"}
]

test_purchase = 300.0

for c in customers:
    tier = c["tier"]
    discount = tier_discounts.get(tier, 0)
    discount_amount = test_purchase * discount
    print(f"Name: {c['name']} | Tier: {tier} | Discount Amount: ${discount_amount:.2f}")


#Exercise 7

catalog = {
    "Widget A": {"price": 9.99, "stock": 150}, 
    "Gadget C": {"price": 49.99, "stock": 8},
}

for product, info in catalog.items():
    if info["stock"] < 20:
        print(f"LOW STOCK ALERT: {product} has only {info['stock']} units left!")


#Exercise 8

transactions = [
    {"region": "South", "amount": 300}, 
    {"region": "North", "amount": 150}, 
    {"region": "South", "amount": 200},
    {"region": "East", "amount": 450},
    {"region": "North", "amount": 75}
]

region_summary = {}

for tx in transactions:
    reg = tx["region"]
    amt = tx["amount"]
    region_summary[reg] = region_summary.get(reg, 0) + amt

for reg in sorted(region_summary.keys()):
    print(f"{reg}: {region_summary[reg]}")