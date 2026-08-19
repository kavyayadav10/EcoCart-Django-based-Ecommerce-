import sqlite3
from datetime import datetime
# Path to your SQLite database
db_path = 'C:/Users/HP PROBOOK/Desktop/db.sqlite3'

# Connect to the SQLite database
connection = sqlite3.connect(db_path)
cursor = connection.cursor()

# Sample data to insert
current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

new_order_products = [
    (1, 101, 2, 5000, "asparagus",current_time,1),  # (order_id, product_id, quantity)
    (2, 102, 1, 2000, "cabbage",current_time,2),
    (3, 103, 5, 2500, "rice",current_time,3),
    (4, 104, 3, 1500, "wheat",current_time,4)
]

# Insert data into orders_orderproduct table
cursor.executemany('''
    INSERT INTO orders_orderproduct (order_id, product_id, quattity,product_price, ordered, created_At, user_id)
    VALUES (?, ?, ?,?,?,?,?)
''', new_order_products)

# Commit the transaction
connection.commit()

# Close the connection
connection.close()

print("Data inserted successfully.")
