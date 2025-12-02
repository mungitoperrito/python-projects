# Fix file and directory naming on Windows


import os
import re

###############
### GLOBALS ###
###############

# Words that have special capitalization
cap_words = {
    "1st":"1st", "2d":"2d", "2nd":"2nd", "3rd":"3rd", "4th":"4th", "5th":"5th",
    "13th":"13th", "31st":"31st", "49th":"49th", "69th":"69th",
    "1s":"1s", "2s":"2s", "3s":"3s", "4s":"4s", "5s":"5s", "6s":"6s", "7s":"7s",
    "1910s":"1910s", "1920s":"1920s", "1930s":"1930s", "1940s":"1940s",
    "1950s":"1950s", "1960s":"1960s", "1970s":"1970s", "1980s":"1980s",
    "1990s":"1990s", "2000s":"2000s", "2010s":"2010s",
    "5.6.7.8s":"5.6.7.8s","10cc":"10CC", "120z":"12oz", "101ers":"101ers",
    "ii":"II", "iii":"III", "iv":"IV", "vi":"VI",
    "vii":"VII", "viii":"VIII", "ix":"IX", "xiv":"XIV",
    "ii.mp3":"II.mp3", "iii.mp3":"III.mp3", "iv.mp3":"IV.mp3",
    "abba":"ABBA", "abc":"ABC", "acdc":"ACDC", "ad":"AD", "adk":"ADK",
    "afi":"AFI", "afu":"AFU", "ags":"AGs","atp":"ATP",
    "albumart.jpg":"AlbumArt.jpg",
    "albumartlarge.jpg":"AlbumArtLarge.jpg",
    "albumartsmall.jpg":"AlbumArtSmall.jpg",
    "bb":"BB", "b-52s":"B-52s", "bap":"BAP", "bbq":"BBQ", "bj":"BJ",
    "boa":"BOA", "br5-49":"BR5-49", "brmc":"BRMC", "bt":"BT", "bto":"BTO",
    "b.u.h":"BUH", "buh":"BUH", "bwv":"BWV",
    "cd":"CD", "cd1":"CD1", "cd2":"CD2", "cd3":"CD3",
    "ca":"CA", "cbc":"CBC", "cbgb":"CBGB", "cbgbs":"CBGBs", "cbmt":"CBMT",
    "cc":"CC", "cia":"CIA", "civ":"CIV", "cky":"CKY", "cm":"CM", "cmx":"CMX",
    "cpe":"CPE", "cpu":"CPU", "cpw":"CPW", "cw":"CW",
    "daf":"DAF", "dbs":"DBs", "ddt":"DDT", "dfl":"DFL", "dhj":"DHJ", "di":"DI",
    "diy":"DIY", "dj":"DJ", "djs":"DJs", "dl":"DL", "dlg":"DLG", "dmc":"DMC",
    "dmz":"DMZ", "dna":"DNA", "doa":"DOA", "doi":"DOI", "dm":"DM",
    "dnce":"DNCE",
    "dph":"DPH", "dr.":"Dr", "dri":"DRI", "dsn":"DSN",
    "ec":"EC", "ecfu":"ECFU", "ef":"EF", "eg":"EG", "ej":"EJ", "elo":"ELO",
    "emi":"EMI", "ep":"EP", "est":"EST",
    "fb":"FB", "fm":"FM", "fod":"FOD", "fus":"FUs",
    "gbh":"GBH", "gc5":"GC5", "gg":"GG", "gh":"GH",
    "h20":"H20", "hwv":"HWV",
    "ibm":"IBM", "id":"ID", "inah":"INAH", "inxs":"INXS",
    "jb":"JB", "jbo":"JBO", "jc":"JC", "jd":"JD", "jfa":"JFA", "jj":"JJ",
    "jls":"JLS", "jvk":"JVK", "jx":"JX",
    "kas":"KAS", "kc":"KC", "kez":"KEZ", "kgb":"KGB", "kkpa":"KKPA",
    "klf":"KLF", "kmc":"KMC", "kmdfm":"KMDFM", "ksu":"KSU", "kxlu":"KXLU",
    "lp":"LP", "lmfao":"LMFAO", "lsd":"LSD", "lse":"LSE", "ltd":"LTD",
    "mc5":"MC5", "mc":"MC", "mdc":"MDC", "mgs":"MGs", "mh":"MH", "mia":"MIA",
    "mod":"MOD", "mph":"MPH",
    "nc":"NC", "nofx":"NOFX", "nota":"NOTA", "nrbq":"NRBQ", "nrm":"NRM", "nsync":"NYSNC",
    "nwa":"NWA", "nj":"NJ", "nrg":"NRG", "ny":"NY", "nyc":"NYC", "nyhc":"NYHC",
    "oclock":"OClock", "od":"OD", "oconnor":"OConnor", "oday":"ODay",
    "odonnell":"ODonnell", "oneal":"ONeal", "oquin":"OQuin",
    "osullivan":"OSullivan",
    "pbr":"PBR", "ped":"PED", "pdq":"PDQ", "pil":"PIL", "plc":"PLC",
    "pox":"POX", "ptl":"PTL", "pva":"PVA", "pvc":"PVC",
    "rb":"RB", "r.e.m.":"REM", "rkl":"RKL", "reo":"REO", "roq":"ROQ",
    "rnb":"RnB", "rpa":"RPA", "rpm":"RPM", "rpms":"RPMS", "rtl":"RTL",
    "rtz":"RTZ", "ru":"RU",
    "sf":"SF", "sh":"SH", "sig":"SIG", "smd":"SMD", "snfu":"SNFU",
    "sncc":"SNCC", "sobo":"SOBO", "sod":"SOD", "src":"SRC", "ss":"SS",
    "ssg":"SSG", "sst":"SST", "stp":"STP",
    "ta80":"TA80", "tc":"TC", "tdk":"TDK", "tj":"TJ", "tnn":"TNN", "tns":"TNS",
    "tpk":"TPK", "tpu":"TPU", "t.s.o.l":"TSOL", "tsol":"TSOL", "tv":"TV",
    "tvo":"TVO", "tx":"TX", "tzn":"TZN",
    "u2":"U2", "ub40":"UB40", "udo":"UDO", "u.f.o":"UFO", "uk":"UK",
    "usa":"USA", "usmc":"USMC", "uxa":"UXA",
    "vs":"vs",
    "wasp":"WASP", "wwi":"WWI", "wwii":"WWII", "wv":"WV",
    "xtc":"XTC", "xxx":"XXX", "xcii":"XCII",
    "yr":"YR",
    "zz":"ZZ"
    }

# Strings that span a space character. Common ending patterns get attached to
#   dates and file extensions: WRSU..1986, Oakland CA.mp3
contractions = {
    "20S":"20s", "30S":"30s", "40S":"40s", "50S":"50s",
    "60S":"60s", "70S":"70s", "80S":"80s", "90S":"90s",
    "Ain T ":"Aint ", "Can T ":"Cant ", "Don T ":"Dont ", "I M ":"Im ",
    "I Ve ":"Ive ", "We Re ":"Were ", "Who S ":"Whos ", "Won T ":"Wont ",
    "You Re ":"Youre ",
    "La Guns":"LA Guns", "La Tour":"LA Tour",
    "Mxpx":"MxPx", "MacUmba":"Macumba",
    " O ":"-O-",
    " S ":"s ", "Spn-X":"SPN-X", "Sr 71":"SR71",
    " Ca.":" CA.", " Ep.":" EP.", " Ma.":" MA.", " Mi.":" MI.", " Ms.":" MS.", " Ny.":" NY.",
    ".Cb ":".CB ", ".Ny ":".NY ",
    "Us Army":"US Army", "Us Bombs":"US Bombs", "Us Chaos":"US Chaos",
    "Us Marine":"US Marine", "Us Roughnecks":"US Roughnecks",
    "Wmbr":"WMBR", "Wfmu":"WFMU", "Wnyu":"WNYU",  "Wrsu":" WRSU", "wpa":"WPA",
    "Xe-None":"Xe-NONE"
    }

# Mac and Mc exceptions
#   Teh function appends a word boundary marker after the search string
mac_and_mc = {
    "MacHine":"Machine", "MacHiavelli":"Machiavelli", "MacH":"Mach",
    "MacHo":"Macho", "MacRo":"Macro", "MacK":"Mack", "MacKs":"Macks",
    "Mackenzie":"MacKenzie", "MacC":"Macc", "MacEo":"Maceo",
    "MacHucambos":"Machucambos", "MacS":"Macs"
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
    remove_char = "@#_\(\);"
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

    # Fix date format
    name = fix_date_format(name)

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
    for k,v in mac_and_mc.items():
        pattern = k + "\\b"
        name = re.sub(pattern, v, name)


    return name


def fix_date_format(name):
    def replace_date(match):
        year = match.group(3)
        month = match.group(1)
        day = match.group(2)

        if len(month) == 1:
            month = "0" + month

        if len(day) == 1:
            day = "0" + day

        return f"{year}-{month}-{day}"

    name = re.sub("(\d+)[.-](\d+)[.-](\d\d\d\d)", replace_date, name)

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
    # print(f"FROM F: {old_name}  TO: {new_path_and_name}")

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
    # print(f"FROM D: {old_name}    TO: {new_path_and_name}")

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