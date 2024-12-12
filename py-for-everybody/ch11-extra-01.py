# regex

import re

fh = open('mbox-short.txt')

# Multiple captures return a single tuple list
for line in fh:
    line = line.rstrip()
    x = re.findall('^From .* ([0-9][0-9]):([0-9][0-9]):([0-9][0-9])', line)
    if len(x) > 0: print(x)
    exit()