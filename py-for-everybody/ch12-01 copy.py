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
import urllib.parse as uparse
import urllib.error as uerror


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
            lines.append(l)
            size += len(l)
    except Exception as e:
        print(f'ERROR: Content missing: {line}')
        print(e)
        exit()

    return lines, size    


############
### MAIN ###
############
url = get_url()
site = get_site(url)
site_content, site_size = get_content(site)

print(site_content)
print(site_size)

# TEST SITES
# http://data.pr4e.org/romeo.txt
# https://docs.python.org
#