# Create random file names to change display ordering.

import os
import uuid

def get_file_list():
   current_dir = os.getcwd()
   files = os.listdir( current_dir )

   return files


if __name__ == '__main__':

   for file in get_file_list():
      if file.endswith('.jpg'):
         # Allows toggle to remove initial random string
         new_file = file

         # # Uncomment to strip initial strings
         # # assumes filenames have been transformed already
         # new_file = file[7:]

         start_string = str(uuid.uuid4())[:5]
         new_name =  start_string + '..' + new_file
         os.rename(file, new_name )
