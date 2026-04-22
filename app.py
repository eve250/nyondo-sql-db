import sqlite3

# Connect to the existing database
conn = sqlite3.connect('nyondo_stock.db')
#securing security
name = input("Enter product name: ")
query = "SELECT * FROM products WHERE name = ?"
##the way i excute here changes too
rows = conn.execute(query, (name,)).fetchall()

for row in rows:
    print(row)

conn.close()
# Close connectionsc
conn.close()