import duckdb

# Connect to the DuckDB database
con = duckdb.connect("olist.db")

# Run a simple query to confirm the connection works
result = con.execute("SELECT 'Connection successful!'").fetchall()

# Print the result
print(result)

# Close the connection
con.close()

