import duckdb

print("Checking for NULL Shipment IDs...")
print("=" * 60)

result = duckdb.query(
    "SELECT * FROM read_csv_auto('Shipments.csv') WHERE Shipment_ID IS NULL"
)

null_count = len(result)
print(f"Total NULL Shipment IDs found: {null_count}")

if null_count > 0:
    print("\nShowing NULL shipment records:")
    result.show()
else:
    print("No NULL Shipment IDs found.")
