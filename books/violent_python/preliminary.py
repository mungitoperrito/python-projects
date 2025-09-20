import socket
import threading
import time

# From text, p10 doesn't work - try to create client - server threads
#
# socket.setdefaulttimeout(2)
# s = socket.socket()
# s.connect(("192.168.0.1", 80))
# ans = s.recv(1024)
# print(ans)
# s.close()

def define_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("localhost", 8083))
    server_socket.listen(5)

    while True:
        connection, address = server_socket.accept()
        buffer = connection.recv(1024)
        if len(buffer) > 0:
            print(buffer)
            break

def define_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("localhost", 8083))
    client_socket.send(b"Hola, hola")

server_thread = threading.Thread(target=define_server)
server_thread.start()

time.sleep(2) # wait for server to start

client_thread = threading.Thread(target=define_client)
client_thread.start()
