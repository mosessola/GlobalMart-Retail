import pandas as pd

print("Loading supplier and product data...")

suppliers = pd.read_csv("Suppliers.csv")
products = pd.read_csv("Products.csv")

invalid_suppliers = products[
    ~products["Supplier_ID"].isin(suppliers["Supplier_ID"])
]

print(f"Invalid Supplier IDs: {len(invalid_suppliers):,}")