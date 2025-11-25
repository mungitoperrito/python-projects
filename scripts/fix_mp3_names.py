# Fix file and directory naming on Windows


import os
import re

###############
### GLOBALS ###
###############

# Words that have special capitalization
cap_words = {
    "1st":"1st", "2d":"2d", "2nd":"2nd", "3rd":"3rd", "4th":"4th",
    "13th":"13th", "31st":"31st", "49th":"49th",
    "30s":"30s", "40s":"40s", "50s":"50s",
    "1910s":"1910s", "1920s":"1920s", "1930s":"1930s", "1940s":"1940s",
    "1950s":"1950s", "1960s":"1960s", "1970s":"1970s", "1980s":"1980s",
    "1990s":"1990s",
    "5.6.7.8s":"5.6.7.8s","10cc":"10CC", "120z":"12oz", "101ers":"101ers",
    "abba":"ABBA", "abc":"ABC", "acdc":"ACDC", "adk":"ADK", "afi":"AFI",
    "afu":"AFU", "ags":"AGs","atp":"ATP",
    "albumartlarge.jpg":"AlbumArtLarge.jpg",
    "albumartsmall.jpg":"AlbumArtSmall.jpg",
    "bb":"BB", "b-52s":"B-52s", "bap":"BAP", "bbq":"BBQ", "boa":"BOA", "br5-49":"BR5-49",
    "brmc":"BRMC", "bt":"BT", "bto":"BTO", "b.u.h":"BUH", "buh":"BUH",
    "bwv":"BWV",
    "cd":"CD", "cd1":"CD1", "cd2":"CD2", "cd3":"CD3",
    "ca":"CA", "cbc":"CBC", "cbgb":"CBGB",
    "cbgbs":"CBGBs", "cbmt":"CBMT", "cia":"CIA", "civ":"CIV", "cky":"CKY",
    "cmx":"CMX", "cpe":"CPE", "cpu":"CPU", "cpw":"CPW",
    "daf":"DAF", "dbs":"DBs", "ddt":"DDT", "dfl":"DFL", "dhj":"DHJ", "di":"DI", "diy":"DIY",
    "dj":"DJ", "djs":"DJs", "dlg":"DLG", "dmz":"DMZ", "doa":"DOA",
    "dnce":"DNCE", "dri":"DRI",
    "ep":"EP",
    "fod":"FOD",
    "ii":"II", "iii":"III", "iv":"IV", "vi":"VI",
    "vii":"VII", "viii":"VIII", "ix":"IX",
    "ii.mp3":"II.mp3", "iii.mp3":"III.mp3", "iv.mp3":"IV.mp3",
    "jfa":"JFA",
    "kc":"KC", "kez":"KEZ", "kxlu":"KXLU", "kmc":"KMC", "kmdfm":"KMDFM",
    "lp":"LP", "lmfao":"LMFAO",
    "mc5":"MC5", "mdc":"MDC", "mgs":"MGs", "mh":"MH", "mia":"MIA", "mph":"MPH",
    "nofx":"NOFX", "nota":"NOTA", "nrbq":"NRBQ", "nrm":"NRM", "nsync":"NYSNC",
    "nwa":"NWA", "nj":"NJ", "ny":"NY", "nyhc":"NYHC",
    "od":"OD",
    "ped":"PED", "pdq":"PDQ", "pox":"POX", "ptl":"PTL",
    "r.e.m.":"REM", "rpm":"RPM",
    "t.s.o.l":"TSOL", "tsol":"TSOL", "tv":"TV",
    "u.f.o":"UFO", "uk":"UK", "usa":"USA",
    "vs":"vs",
    "wmbr":"WMBR", "wnyu":"WNYU",  "wrsu":"WRSU",
    }

# Strings that span a space character
contractions = {
    "60s":"60s", "70s":"70s", "80s":"80s",
    "Ain T ":"Aint ", "Can T ":"Cant ", "Don T ":"Dont ",
    "I M ":"Im ", "I Ve ":"Ive", "We Re ":"Were ", "Won T ":"Wont ",
    "You Re ":"Youre ",
    "La Guns":"LA Guns", " O ":"-O-",
    " S ":"s ", "Sr 71":"SR71"
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

    # Change & to and
    name = name.replace('&', 'and')

    # Title case for body
    name = name.title()

    # Fix special capitalization
    name = fix_special_capitalization(name)

    # Fix contractions
    for c in contractions.keys():
        name = name.replace(c, contractions[c])

    # Fix Mc Mac
    name = fix_mc_mac(name)

    # Compress extra white space
    name = ' '.join(name.split())

    return name


def fix_special_capitalization(name):
    words = name.split()
    new_name = ''
    for w in words:
        if w.lower() in cap_words.keys():
            w = cap_words[w.lower()]
        new_name += ' ' + w
    name = new_name

    return name


def fix_mc_mac(name):
    def replace_upper(match):
        return match.group(1) + match.group(2).upper()

    name = re.sub("(Mc)([a-z])", replace_upper, name)
    name = re.sub("(Mac)([a-z])", replace_upper, name)

    # Exceptions
    name = re.sub("MacHine", "Machine", name)
    name = re.sub("MacHiavelli", "Machiavelli", name)
    name = re.sub("MacH ", "Mach ", name)
    name = re.sub("MacHo ", "Macho ", name)
    name = re.sub("MacRo", "Macro", name)
    name = re.sub("MacK ", "Mack ", name)
    name = re.sub("MacKenzie", "Mackenzie", name)

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
    #    Form 1: AlbumArt{1234}Small.jpg
    #    Form 2: AlbumArt_{1234}_Small.jpg
    if "lbum" in name:
        name = re.sub('(_|\s)*\{.*\}(_|\s)*', '', name)

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

                # Drop duplicated album art files
                if re.match("Album.*jpg", name):
                    try:
                        os.remove(old_path_and_name)
                    except Exception as e:
                        print(f"ERR: Can't remove {old_path_and_name}")
                        print(f"ERR: {e}")
                else:
                    # Label potential duplicate files
                    new_path_and_name += ".DUP_FILE_NAME"

                    # mp3 extension improves detailed display in Windows
                    if extension == ".mp3":
                        new_path_and_name += ".mp3"
                    print(f"FILE DUP: {new_path_and_name}")

        try:
            if os.path.exists(old_path_and_name):
                os.rename(old_path_and_name, new_path_and_name)
        except Exception as e:
            print(f"ERR: Can't rename {old_path_and_name}  {new_path_and_name}")
            print(f"ERR: {e}")


def update_dir_names(name):
    # Preserve original name
    old_path_and_name = name
    old_path = os.path.dirname(name)
    old_name = os.path.basename(name)

    # Get filename, drop path for changes
    name = old_name

    # Changes that are the same for files and dirs
    name = make_common_changes(name)

    # Capitalize NOW
    match = re.search('Now \d', name)
    if match:
        name = name.replace('Now ', 'NOW ')

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
                print(f"DIR DUP: {new_path_and_name}")

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