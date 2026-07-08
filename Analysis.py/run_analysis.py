
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