# https://www.py4e.com/html3/12-network
# Exercise 3

'''
Use urllib to replicate the previous exercise of (1) retrieving the
document from a URL, (2) displaying up to 3000 characters, and (3)
counting the overall number of characters in the document. Don’t worry
about the headers for this exercise, simply show the first 3000
characters of the document contents.
'''
import urllib.request as urequest

def get_url():
    while True:
        url = input('Enter a URL: ')
        if len(url) == 0:
            continue
        if url.startswith('http') != True:
            continue
        
        return url


def get_site(url):
    try:
        site = urequest.urlopen(url)
    except Exception as e:
        print(f'ERROR: Site not found: {url}')
        print(e)
        exit()

    return site


def get_content(site):
    lines = list()
    size = 0

    try:
        for line in site:
            l = line.decode()
            lines.append(l.rstrip())
            size += len(l)
    except Exception as e:
        print(f'ERROR: Content missing: {line}')
        print(e)
        exit()

    return lines, size    


def print_to_count(input_list, count):
    # Assumes the input is a list of strings
    count_so_far = 0

    for line in input_list:
        if count_so_far < count:
            if len(line) + count_so_far <= count:
                print(line)
                count_so_far += len(line)
            else:
                up_to = count - count_so_far + 1
                print(line[:up_to])
                return
    


############
### MAIN ###
############
url = get_url()
site = get_site(url)
site_content, site_size = get_content(site)
characters_to_print = 3000

# print(site_content)
print_to_count(site_content, characters_to_print)
print(site_size)

# TEST SITES
# http://data.pr4e.org/romeo.txt
# https://docs.python.org
#