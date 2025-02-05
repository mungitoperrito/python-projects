# https://www.py4e.com/html3/10-tuples
# exercise 3

def get_file_handle(filename):
    try:
        fh = open(filename, encoding="utf8")
    except Exception as e:
        print(f"Can't open: {filename}.")
        print(f"Error: {e}")
        exit()

    return fh

def get_letter_counts(filehandle):
    letters = dict()

    for line in filehandle.readlines():
        this_line = list(line.lower())
        for letter in this_line:
            if letter.isalpha():
                letters[letter] = letters.get(letter, 0) + 1
                if letter.isdigit():
                    print(f"ERROR: {letter}") ; exit() ; #DEBUG    
    return letters        

def sort_dictionary(dictionary):
    tmp_list = list()
    return_dict = dict()

    for k,v in dictionary.items():
        tmp_list.append( (k, v) )

    tmp_list.sort()

    for t in tmp_list:
        k, v = t
        return_dict[k] = v

    return return_dict


def join_dictionaries(list_of_dicts):
    header = ['letter']
    combined = dict()
    num_dicts = len(list_of_dicts)
    default_counts = [0 for x in range(num_dicts)]
    # print(default_counts) ; exit()

    this_dict_number = 0
    for d in list_of_dicts:
        lang, counts = d
        header.append(lang[:-4])

        for k, v in counts.items():
            # Copy the list or later values overwrite the reference
            current_totals = combined.get(k, default_counts)[:]
            current_totals[this_dict_number] = v
            combined[k] = current_totals
        
        this_dict_number += 1

        # print(combined) ; exit()
    return header, combined


############
### MAIN ###
############
sample_files = ['english.txt', 'french.txt', 'spanish.txt', 'swedish.txt']
# sample_files = ['english.txt']
counts_by_language = list()

for sf in sample_files:
    fh = get_file_handle(sf)

    letter_counts = get_letter_counts(fh)
    letter_counts_sorted = sort_dictionary(letter_counts)

    # print(f"{sf}: {letter_counts_sorted}")
    # print()
    counts_by_language.append((sf, letter_counts_sorted))
  
header, combined = join_dictionaries(counts_by_language)

for h in header:
    print(f"{h.ljust(10, ' ')}", end='')
print()

for ltr, vals in combined.items():
    print(f"{ltr.ljust(10, ' ')}", end='')
    for v in vals:
        print(f"{str(v).ljust(10, ' ')}", end='')
    print()