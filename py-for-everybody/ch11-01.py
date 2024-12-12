# https://www.py4e.com/html3/11-regex
# exercise 1

import sys
import re

def check_args():
    if len(sys.argv) != 3:
        print("Usage:  ch11-01.py regex filename.")
        exit()

    
def get_file_handle(): 
    try:
        fh = open(sys.argv[2])       
    except Exception as e:
        print(f"Error: {e}")
        exit()

    return fh

def get_regex():
    return sys.argv[1]    
 
    # NOTE: windows needs " instead of ' for initial ^


def search_file():
    search_results = []
    fh = get_file_handle()
    re_expr = get_regex()
    print(re_expr)

    for line in fh.readlines():
        # Returns None or a match object
        results_this_line = re.search(re_expr, line)
        if results_this_line != None:
            # Preserve trailing spaces in target line
            search_results.append(results_this_line.string.rstrip('\n'))

    return search_results

############
### MAIN ###
############
check_args()
results = search_file()

for r in results:
    print(r)
