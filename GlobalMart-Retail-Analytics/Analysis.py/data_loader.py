import pandas as pd

def load_data():

    customers = pd.read_csv("Customers.csv")
    forecast = pd.read_csv("Forecast.csv")
    inventory = pd.read_csv("Inventory.csv")

    orders1 = pd.read_csv("Orders_part1.csv")
    orders2 = pd.read_csv("Orders_part2.csv")
    orders3 = pd.read_csv("Orders_part3.csv")
    orders4 = pd.read_csv("Orders_part4.csv")

    orders = pd.concat(
        [orders1, orders2, orders3, orders4],
        ignore_index=True
    )

    products = pd.read_csv("Products.csv")
    shipments = pd.read_csv("Shipments.csv")
    stores = pd.read_csv("Stores.csv")
    suppliers = pd.read_csv("Suppliers.csv")

    return (
        customers,
        forecast,
        inventory,
        orders,
        products,
        shipments,
        stores,
        suppliers
    )