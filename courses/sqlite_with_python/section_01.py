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

# Create a table
# Check if table exists first
exists = cursor.execute('''
    SELECT COUNT(name)
    FROM sqlite_master
    WHERE type='table' AND name='customers';
''')

if exists.fetchall()[0][0] == False:
    print('Create customers table')
    cursor.execute('''
    CREATE TABLE customers(
        first_name TEXT,
        last_name TEXT,
        email TEXT
        )
    ''')

# # Uncomment to drop the table
# cursor.execute('''
#     DROP TABLE IF EXISTS 'customers';
# ''')


# Commit the changes
db.commit()

# Close the db connection
db.close()