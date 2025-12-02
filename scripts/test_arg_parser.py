# Test argparser function

import argparse

parser = argparse.ArgumentParser(description="Test argparse")
parser.add_argument("--run", type=bool, default=False)
args = parser.parse_args()

print(f"AR: {args.run}")

if args.run == True:
    print("True")
else:
    print("False")

###############
### RESULTS ###
'''
# No arg defaults to False
python3 /mnt/e/MUSIC/__Scripts/test_arg_parser.py
AR: False
False

# Must supply a value with arg
python3 /mnt/e/MUSIC/__Scripts/test_arg_parser.py --run
usage: test_arg_parser.py [-h] [--run RUN]
test_arg_parser.py: error: argument --run: expected one argument

# DANGER: *ANY* value makes run True
python3 /mnt/e/MUSIC/__Scripts/test_arg_parser.py --run False
AR: True
True

# DANGER: *ANY* value makes run True
python3 /mnt/e/MUSIC/__Scripts/test_arg_parser.py --run Blah
AR: True
True
'''