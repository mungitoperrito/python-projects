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

# Insert rows
#    sqlite isn't inserting duplicate rows after renunning the script.
#    Don't know why
cursor.execute('''
    INSERT INTO customers
    VALUES ("Joey", "Ramone", "joey@ceebees.com"),
           ("Johnny", "Ramone", "johnny@ceebees.com"),
           ("Dee Dee", "Ramone", "deedee@ceebees.com"),
           ("Tommy", "Ramone", "tommy@ceebees.com"),
           ("Marky", "Ramone", "marky@ceebees.com");
''')

row_count = cursor.execute('SELECT COUNT(*) FROM customers;')
print(row_count.fetchone()[0])

view_table = cursor.execute('SELECT * FROM customers;')
print(view_table.fetchone())

# Close the db connection
db.close()