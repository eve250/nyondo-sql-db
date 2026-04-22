import sqlite3

# Connect to the existing database
conn = sqlite3.connect('nyondo_stock.db')

# Take user input
name = input("Enter product name: ")

# ❌ Vulnerable query (SQL injection possible)
query = "SELECT * FROM products WHERE name = '" + name + "'"

# Execute query
rows = conn.execute(query).fetchall()

# Display results
for row in rows:
    print(row)

# Close connectionsc
conn.close()