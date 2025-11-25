import re

def fix_mc_mac(name):
    def replace_upper(match):
        print(f"M: '{match}'")
        print(f"MG1: '{match.group(1)}'")
        print(f"MG2: '{match.group(2)}'")
        return match.group(1) + match.group(2).upper()

    name = re.sub("(Mc)([a-z])", replace_upper, name)
    print("1")
    name = re.sub("(Mac)([a-z])", replace_upper, name)
    print("2")
    print(f"BE: {name}")

    # Exceptions
    name = re.sub("MacHine", "Machine", name)
    name = re.sub("MacHiavelli", "Machiavelli", name)
    name = re.sub("MacH ", "Mach ", name)
    name = re.sub("MacHo ", "Macho ", name)
    name = re.sub("MacRo", "Macro", name)
    name = re.sub("MacK ", "Mack ", name)
    name = re.sub("MacKenzie", "Mackenzie", name)

    return name


names = [
         "Mc ", "Mac ",
         "McTell", "McOff",
         "Mack ", "Mackenzie", "MacKay",
         "Macro",
         "Machine", "Mach ", "Macho ", "MacHowe"
        ]

for name in names:
    print(f"N: '{name}'")
    print(f"F: '{fix_mc_mac(name)}'")
    print("")