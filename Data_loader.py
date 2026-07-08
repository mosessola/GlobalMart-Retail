import pandas as pd

print("Loading datasets...")

customers = pd.read_csv("Customers.csv")
forecast = pd.read_csv("Forecast.csv")
inventory = pd.read_csv("Inventory.csv")

orders1 = pd.read_csv("Orders_part1.csv")
orders2 = pd.read_csv("Orders_part2.csv")
orders3 = pd.read_csv("Orders_part3.csv")
orders4 = pd.read_csv("Orders_part4.csv")

products = pd.read_csv("Products.csv")
shipments = pd.read_csv("Shipments.csv")
stores = pd.read_csv("Stores.csv")
suppliers = pd.read_csv("Suppliers.csv")

print("Datasets loaded successfully!")

print()

print("Customers:", customers.shape)
print("Forecast:", forecast.shape)
print("Inventory:", inventory.shape)
print("Orders1:", orders1.shape)
print("Orders2:", orders2.shape)
print("Orders3:", orders3.shape)
print("Orders4:", orders4.shape)
print("Products:", products.shape)
print("Shipments:", shipments.shape)
print("Stores:", stores.shape)
print("Suppliers:", suppliers.shape)
import pandas as pd

print("=" * 60)
print("LOADING DATASETS")
print("=" * 60)

customers = pd.read_csv("Customers.csv")
forecast = pd.read_csv("Forecast.csv")
inventory = pd.read_csv("Inventory.csv")

orders1 = pd.read_csv("Orders_part1.csv")
orders2 = pd.read_csv("Orders_part2.csv")
orders3 = pd.read_csv("Orders_part3.csv")
orders4 = pd.read_csv("Orders_part4.csv")

orders = pd.concat([orders1, orders2, orders3, orders4], ignore_index=True)

products = pd.read_csv("Products.csv")
shipments = pd.read_csv("Shipments.csv")
stores = pd.read_csv("Stores.csv")
suppliers = pd.read_csv("Suppliers.csv")

datasets = {
    "Customers": customers,
    "Forecast": forecast,
    "Inventory": inventory,
    "Orders": orders,
    "Products": products,
    "Shipments": shipments,
    "Stores": stores,
    "Suppliers": suppliers,
}

print("\nDatasets Loaded Successfully\n")

for name, df in datasets.items():
    print(f"{name:<12} Rows: {len(df):>10,}   Columns: {df.shape[1]}")
    import pandas as pd


def profile(df, name):

    print("\n" + "=" * 70)
    print(name.upper())
    print("=" * 70)

    print("\nShape")
    print(df.shape)

    print("\nMissing Values")
    print(df.isnull().sum())

    print("\nDuplicate Rows")
    print(df.duplicated().sum())

    print("\nData Types")
    print(df.dtypes)

    print("\nSummary Statistics")
    print(df.describe(include="all"))


profile(customers, "Customers")
profile(orders, "Orders")
profile(products, "Products")
print("\n" + "=" * 60)
print("SELLING PRICE CHECK")
print("=" * 60)

bad_prices = products[
    products["Selling_Price"] < products["Cost_Price"]
]

print(f"Products sold below cost: {len(bad_prices):,}")
print("Reached Revenue Validation")

print("\n" + "=" * 60)
print("VALIDATING REVENUE")
print("=" * 60)

calculated_revenue = orders["Quantity"] * orders["Unit_Price"]

incorrect_revenue = orders[
    abs(calculated_revenue - orders["Revenue"]) > 0.01
]

print(f"Incorrect Revenue Records: {len(incorrect_revenue):,}")

print("Revenue Validation Finished")

print("Starting Profit Validation")

print("\n" + "=" * 60)
print("VALIDATING PROFIT")
print("=" * 60)

calculated_profit = orders["Revenue"] - orders["Cost"]

incorrect_profit = orders[
    abs(calculated_profit - orders["Profit"]) > 0.01
]
print(f"Incorrect Profit Records: {len(incorrect_profit):,}")
