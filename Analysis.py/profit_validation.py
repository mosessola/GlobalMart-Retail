import pandas as pd

print("Loading Orders data...")

orders1 = pd.read_csv("Orders_part1.csv")
orders2 = pd.read_csv("Orders_part2.csv")
orders3 = pd.read_csv("Orders_part3.csv")
orders4 = pd.read_csv("Orders_part4.csv")

orders = pd.concat([orders1, orders2, orders3, orders4], ignore_index=True)

print("Orders loaded successfully!")
print("\n" + "=" * 60)
print("VALIDATING PROFIT")
print("=" * 60)

calculated_profit = (
    orders["Revenue"]
    - orders["Cost"]
    - orders["Shipping_Cost"]
).round(2)

incorrect_profit = orders[
    abs(calculated_profit - orders["Profit"]) > 0.01
]

print(f"Incorrect Profit Records: {len(incorrect_profit):,}")