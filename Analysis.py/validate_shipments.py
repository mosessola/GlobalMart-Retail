import pandas as pd

print("Loading shipment data...")

shipments = pd.read_csv("Shipments.csv")
stores = pd.read_csv("Stores.csv")
suppliers = pd.read_csv("Suppliers.csv")

print("Datasets loaded.\n")

print("="*60)
print("SHIPMENT VALIDATION")
print("="*60)

# Supplier check
invalid_supplier = shipments[
    ~shipments["Supplier_ID"].isin(suppliers["Supplier_ID"])
]

print(f"Invalid Supplier IDs : {len(invalid_supplier):,}")

# Store check
invalid_store = shipments[
    ~shipments["Store_ID"].isin(stores["Store_ID"])
]

print(f"Invalid Store IDs    : {len(invalid_store):,}")

# Date check
shipments["Ship_Date"] = pd.to_datetime(shipments["Ship_Date"])
shipments["Delivery_Date"] = pd.to_datetime(shipments["Delivery_Date"])

bad_dates = shipments[
    shipments["Delivery_Date"] < shipments["Ship_Date"]
]

print(f"Invalid Dates        : {len(bad_dates):,}")

# Shipping Cost
bad_shipping = shipments[
    shipments["Shipping_Cost"] <= 0
]

print(f"Invalid Shipping Cost: {len(bad_shipping):,}")

# Distance
bad_distance = shipments[
    shipments["Distance"] <= 0
]

print(f"Invalid Distance     : {len(bad_distance):,}")