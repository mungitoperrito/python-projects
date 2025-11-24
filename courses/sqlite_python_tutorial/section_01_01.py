import os
import sqlite3

if __name__ == "__main__":

   db_name = "TheWorst"

   try:
      with sqlite3.connect(db_name) as conn:
         print(f"Opened connection to: {db_name}")
   except sqlite3.OperationalError as e:
      print(f"Failed to open {db_name}: ", e)

   # # Uncomment to confirm db file exists
   # print(f"Current directory: {os.getcwd()}")
   # print(f"{db_name} exists: {os.path.isfile(db_name)}")
