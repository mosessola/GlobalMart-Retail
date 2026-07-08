import pandas as pd

print("Loading orders and store data...")

orders1 = pd.read_csv("Orders_part1.csv")
orders2 = pd.read_csv("Orders_part2.csv")
orders3 = pd.read_csv("Orders_part3.csv")
orders4 = pd.read_csv("Orders_part4.csv")
orders = pd.concat([orders1, orders2, orders3, orders4], ignore_index=True)

stores = pd.read_csv("Stores.csv")

invalid_stores = orders[
    ~orders["Store_ID"].isin(stores["Store_ID"])
]

print(f"Invalid Store IDs: {len(invalid_stores):,}")