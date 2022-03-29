# echo-client.py

import socket
import sys

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 8000  # The port used by the server

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect((HOST, PORT))

while True:
    message = sys.stdin.readline()
    server.send(message.encode('utf-8'))

'''with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b"Hello, world")
    data = s.recv(1024)

print(f"Received {data!r}")'''