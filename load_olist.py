import duckdb
import os

# Path to CSV files
csv_folder = "/Users/rubiyahbiamin/DSAI-Group2/data"

# List of CSV files to load to DB
csv_files = [
    "olist_customers.csv",
    "olist_geolocation.csv",
    "olist_order_items.csv",
    "olist_order_payments.csv",
    "olist_order_reviews.csv",
    "olist_orders.csv",
    "olist_products.csv",
    "olist_sellers.csv"
    ]

# Connect to DuckDB database file
conn = duckdb.connect("olist.db")

# Loop over each CSV file and create respective table in DuckDB
for csv_file in csv_files:
    table_name = os.path.splitext(csv_file)[0]  # table name = filename without .csv
    csv_path = os.path.join(csv_folder, csv_file)
    
    conn.execute(f"""
        CREATE OR REPLACE TABLE {table_name} AS
        SELECT *
        FROM read_csv_auto('{csv_path}');
    """)

# Confirm the tables were created
tables = conn.execute("SHOW TABLES;").fetchall()
print("Tables in DuckDB:", tables)

# Close the DB connection 
conn.close()