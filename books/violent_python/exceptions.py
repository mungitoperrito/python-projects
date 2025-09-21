import socket

# Check for time outs
try:
    socket.setdefaulttimeout(2)
    s = socket.socket()
    # s.connect(("192.168.95.149", 21)) # Book site not running
    s.connect(("49.12.121.47", 21))     # FileZilla site
    ans = s.recv(1024)
    print(ans)
    s.close()
except socket.timeout as e:
    print("Time out error:", e)


# # Output
# # Working
# b'220 FZ router and firewall tester ready\r\n'

# # Error
# Time out error: timed out