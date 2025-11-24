# Fix file and directory naming on Windows


import os
import re

###############
### GLOBALS ###
###############

# Words that have special capitalization
cap_words = {
    "1st":"1st", "2d":"2d", "2nd":"2nd", "3rd":"3rd", "4th":"4th",
    "10cc":"10CC", "120z":"12oz", "13th":"13th", "31st":"31st",
    "49th":"49th", "101ers":"101ers",
    "1910s":"1910s", "1920s":"1920s", "1930s":"1930s", "1940s":"1940s",
    "1950s":"1950s", "1960s":"1960s", "1970s":"1970s", "1980s":"1980s",
    "1990s":"1990s",
    "acdc":"ACDC", "afi":"AFI", "afu":"AFU", "ags":"AGs",
    "albumartlarge.jpg":"AlbumArtLarge.jpg",
    "albumartsmall.jpg":"AlbumArtSmall.jpg",
    "bap":"BAP", "bbq":"BBQ", "b.u.h":"BUH",
    "cd1":"CD1", "cd2":"CD2", "cd3":"CD3",
    "dbs":"DBs", "dj":"DJ", "djs":"DJs",
    "ep":"EP",
    "kez":"KEZ", "kxlu":"KXLU",
    "lp":"LP",
    "mh":"MH",
    "wrsu":"WRSU"
    }

#################
### FUNCTIONS ###
#################

def get_starting_directory():
    return os.getcwd()

def make_common_changes(name):
    # Delete unwanted characters
    remove_char = "'’,"
    for c in remove_char:
       name = name.replace(c, '')

    # Change unwanted characters to blanks
    remove_char = "@#_\(\)"
    for c in remove_char:
       name = name.replace(c, ' ')

    # Title case for body
    name = name.title()

    # Fix special capitalization
    words = name.split()
    new_name = ''
    for w in words:
        if w.lower() in cap_words.keys():
            w = cap_words[w.lower()]
        new_name += ' ' + w
    name = new_name

    # Fix contractions
    contractions = {
        "Ain T ":"Aint ", "Can T ":"Cant ", "Don T ":"Dont ", "I M ":"Im ",
        "I Ve ":"Ive", " O ":"-O-", "Won T ":"Wont ", "You Re ":"Youre "
        }
    for c in contractions.keys():
        name = name.replace(c, contractions[c])

    # Compress extra white space
    name = ' '.join(name.split())

    return name


def update_file_names(name):
    # Preserve original name and path
    old_path_and_name = name
    old_path = os.path.dirname(name)
    old_name = os.path.basename(name)

    # Get filename, drop path for changes
    name = old_name

    # Changes that are the same for files and dirs
    name = make_common_changes(name)

    # Delete unwanted art ID strings
    name = re.sub('_\{.*\}_', '', name)

    # Title case for body, extension lower case
    base, extension = os.path.splitext(name)
    extension = extension.lower()
    name = base + extension

    # Full path for file
    new_path_and_name = os.path.join(old_path, name)

    # # Uncomment to test changes
    # print(f"FROM F: {old_name}  TO: {path_and_name}")

    # Uncomment to update files
    if old_name != name:
        if os.path.exists(new_path_and_name):
            # Check lowercase, Windows isn't case sensitive
            if old_name.lower() != name.lower():
                new_path_and_name += ".DUP_FILE_NAME"

        os.rename(old_path_and_name, new_path_and_name)


def update_dir_names(name):
    # Preserve original name
    old_path_and_name = name
    old_path = os.path.dirname(name)
    old_name = os.path.basename(name)

    # Get filename, drop path for changes
    name = old_name

    # Changes that are the same for files and dirs
    name = make_common_changes(name)

    # Full path for dir
    new_path_and_name = os.path.join(old_path, name)

    # # Uncomment to test changes
    # print(f"FROM D: {old_name}    TO: {path_and_name}")

    # Uncomment to update directories
    if old_name != name:
        if os.path.exists(new_path_and_name):
            # Check lowercase, Windows isn't case sensitive
            if old_name.lower() != name.lower():
                new_path_and_name += ".DUP_DIR_NAME"

        os.rename(old_path_and_name, new_path_and_name)


def walk_directories(directory):
    for root, dirs, files in os.walk(directory, topdown=False):

       # Update leaves (files) first
        for f in files:
            # # Uncomment to debug
            # print(os.path.join(root, f))
            update_file_names(os.path.join(root, f))

        # Update dirs
        for d in dirs:
            # # Uncomment to debug
            # print(os.path.join(root, d))
            update_dir_names(os.path.join(root, d))


if __name__ == '__main__':

    start_dir = get_starting_directory()
    walk_directories(start_dir)