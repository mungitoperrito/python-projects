import sqlite3

# Project path
PROJECT_PATH='e:/FILES/projects/python-projects/sqlite_with_python/'

# Connect to dbase on disk
db = sqlite3.connect(PROJECT_PATH + 'customer.db')

# # Connect to dbase in-memory
# db = sqlite3.connect(':memory:')

# # Uncomment to show SQL commands as they are executed
# db.set_trace_callback(print)

# Create a cursor
cursor = db.cursor()

# # Uncomment to see table and row ids
# view_table = cursor.execute('SELECT rowid, * FROM customers;')
# print(view_table.fetchall())

# Delete rows
cursor.execute('''
    DELETE FROM customers
    WHERE email = "marky@ceebees.com"
    ''')

cursor.execute('SELECT * FROM customers;')
rows = cursor.fetchall()
for row in rows:
    print(row)
print()

# # Uncommen to commit the changes
# db.commit()

# Close the db connection
db.close()