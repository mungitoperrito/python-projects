# regex

import re

fh = open('mbox-short.txt')
for line in fh:
    line = line.rstrip()
    # Multiple captures return a single tuple list
    x = re.findall('^From .* ([0-9][0-9]):([0-9][0-9]):([0-9][0-9])', line)
    if len(x) > 0: print(x)