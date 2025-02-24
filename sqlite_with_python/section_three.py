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

# Select rows
tmp = cursor.execute('''
    SELECT *
    FROM customers
    WHERE last_name LIKE "Ram%";
    ''')
rows = tmp.fetchall()
for row in rows:
    print(row)
print()

# Select one
#     Just returns the one item, not the cursor object
one_row = cursor.execute('''
    SELECT *
    FROM customers
    WHERE last_name LIKE "Ram%";
    ''').fetchone()
print(one_row)
print()

# Select multiple
#     Just returns the list, not the cursor object
many_rows = cursor.execute('''
    SELECT *
    FROM customers
    WHERE last_name LIKE "Ram%";
    ''').fetchmany(3)
for row in many_rows:
    print(row)
print()

# Close the db connection
db.close()