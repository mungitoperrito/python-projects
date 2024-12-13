# https://www.py4e.com/html3/12-network
# Exercise 3

'''
Use urllib to replicate the previous exercise of (1) retrieving the
document from a URL, (2) displaying up to 3000 characters, and (3)
counting the overall number of characters in the document. Don’t worry
about the headers for this exercise, simply show the first 3000
characters of the document contents.
'''

import socket

needs_url = True
while needs_url:
     full_url = input('Enter a URL: ')
     if len(full_url) == 0:
         continue
     if full_url.startswith('http') != True:
         continue
     
     needs_url = False

url = full_url.split('/')[2]

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    mysock.connect((url, 80))
except Exception as e:
    print(f'ERROR: URL not found: {url}')
    print(e)
    exit()

try:
    # cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
    cmd = 'GET' + full_url + 'HTTP/1.0\r\n\r\n'
    cmd = cmd.encode()
    mysock.send(cmd)
except Exception as e:
    print(f'ERROR: Full URL not found: {full_url}')
    print(e)
    exit()

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')

mysock.close()

# Code: https://www.py4e.com/code3/socket1.py