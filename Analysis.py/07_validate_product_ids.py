import pandas as pd

products = pd.read_csv("Products.csv")

orders = pd.concat([
    pd.read_csv("Orders_part1.csv"),
    pd.read_csv("Orders_part2.csv"),
    pd.read_csv("Orders_part3.csv"),
    pd.read_csv("Orders_part4.csv")
], ignore_index=True)

print("=" * 60)
print("PRODUCT ID VALIDATION")
print("=" * 60)

invalid_products = orders[
    ~orders["Product_ID"].isin(products["Product_ID"])
]

print(f"Invalid Product IDs: {len(invalid_products):,}")