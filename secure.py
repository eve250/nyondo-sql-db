import sqlite3

conn = sqlite3.connect('nyondo_stock.db')

def search_product_safe(name):
    if not isinstance(name, str):
      print("Name must be a string")

    elif len(name) < 2:
       print("Name must be at least 2 characters")

    elif "<" in name or ">" in name or ";" in name:
        print("Name must not contain < > or ;")

    else:
      print("Valid name")
    query = "SELECT * FROM products WHERE name LIKE ?"
    param = f"%{name}%"
    print(f"Query: {query}")
    rows = conn.execute(query, (param,)).fetchall()
    print(f"Result: {rows}\n")
    return rows

def login_safe(username, password):
    if not isinstance(username, str):
      print("Username must be a string")

    elif username == "":
      print("Username must not be empty")

    elif " " in username:
       print("Username must not contain spaces")

    else:
       print("Valid username")
    query = "SELECT * FROM users WHERE username=? AND password=?"

    print(f"Query: {query}")
    row = conn.execute(query, (username, password)).fetchone()
    print(f"Result: {row}\n")
    return row

# Tests
print('Test 1:', search_product_safe("' OR 1=1--"))
print('Test 2:', search_product_safe("' UNION SELECT id,username,password,role FROM users--"))
print('Test 3:', login_safe("admin'--", 'anything'))
print('Test 4:', login_safe("' OR '1'='1", "' OR '1'='1"))