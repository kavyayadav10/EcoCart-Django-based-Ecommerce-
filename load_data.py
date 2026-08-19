import sqlite3
import pandas as pd
#extract data from database

# Path to your SQLite database
db_path = 'C:/Users/HP PROBOOK/Desktop/db.sqlite3'

# Connect to the SQLite database
connection = sqlite3.connect(db_path)

# Write your SQL query to extract the necessary data
query = '''
SELECT order_id, product_id FROM orders_orderproduct;
'''

# Load data into a pandas DataFrame
data = pd.read_sql_query(query, connection)

# Close the connection
connection.close()

# Print the DataFrame to verify the data
print(data.head())
