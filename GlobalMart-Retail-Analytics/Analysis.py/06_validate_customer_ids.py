import pandas as pd

print("Loading datasets...")

customers = pd.read_csv("Customers.csv")

orders = pd.concat([
    pd.read_csv("Orders_part1.csv"),
    pd.read_csv("Orders_part2.csv"),
    pd.read_csv("Orders_part3.csv"),
    pd.read_csv("Orders_part4.csv")
], ignore_index=True)

print("Datasets loaded.\n")

print("=" * 60)
print("CUSTOMER ID VALIDATION")
print("=" * 60)

invalid_customers = orders[
    ~orders["Customer_ID"].isin(customers["Customer_ID"])
]

print(f"Invalid Customer IDs: {len(invalid_customers):,}")