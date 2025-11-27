# Swap "last_name first_name" to be "first_name last_name"
#   also handle "last_name first_name second_name"

import os
import argparse

parser = argparse.ArgumentParser(description="Move first word to end.")
parser.add_argument("--run", type=bool, default=False)
args = parser.parse_args()

entities = os.listdir()

for ent in entities:
    words = ent.split()
    new_ent = words[len(words)-1] + ' '
    new_ent += ' '.join(words[0:len(words)-1])


    # run defaults to False
    if args.run == True:
        try:
            os.rename(ent, new_ent)
        except Exception as err:
            print(f"Can't rename {ent} to {new_ent}: err")
    else:
        print(f"orig: {ent}   new: '{new_ent}'")
