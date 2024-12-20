# https://www.py4e.com/html3/10-tuples
# exercise 2

def get_file_handle(filename):
    try:
        fh = open(filename)
    except Exception as e:
        print(f"Can't open: {filename}.")
        print(f"Error: {e}")
        exit()

    return fh

def get_hour_counts(filehandle):
    hours = dict()

    for line in filehandle.readlines():
        if line.startswith('From '):
            this_timestamp = line.split()[5]
            this_hour = this_timestamp.split(':')[0]
            hours[this_hour] = hours.get(this_hour, 0) + 1

    return hours        

def sort_by_value(dictionary):
    tmp_list = list()
    return_dict = dict()

    for k,v in dictionary.items():
        tmp_list.append( (k, v) )

    tmp_list.sort()

    for t in tmp_list:
        k, v = t
        return_dict[k] = v

    return return_dict


############
### MAIN ###
############
fh = get_file_handle('mbox-short.txt')

hour_counts = get_hour_counts(fh)
hour_counts_by_value = sort_by_value(hour_counts)

# print(hour_counts)
print(hour_counts_by_value)