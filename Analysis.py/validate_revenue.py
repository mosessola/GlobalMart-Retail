import pandas as pd

print("Loading Orders data...")

orders1 = pd.read_csv("Orders_part1.csv")
orders2 = pd.read_csv("Orders_part2.csv")
orders3 = pd.read_csv("Orders_part3.csv")
orders4 = pd.read_csv("Orders_part4.csv")

Orders = pd.concat([orders1, orders2, orders3, orders4], ignore_index=True)

print("Orders loaded successfully!")
print("\n" + "=" * 60)
print("VALIDATING REVENUE")
print("=" * 60)

calculated_revenue = (
    Orders["Quantity"]
    * Orders["Unit_Price"]
    * (1 - Orders["Discount"])
).round(2)

incorrect_revenue = Orders[
    abs(calculated_revenue - Orders["Revenue"]) > 0.01
]

print(f"Incorrect Revenue Records: {len(incorrect_revenue):,}")