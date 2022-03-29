# echo-server.py

import socket
from _thread import *
import sys

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 8000  # Port to listen on (non-privileged ports are > 1023)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((HOST, PORT))

server.listen(100)
 
list_of_clients = []
 
def clientthread(conn, addr):
    # sends a message to the client whose user object is conn
    message = "Welcome to this chatroom!"
    conn.send(message.encode('utf-8'))

    while True: 
        try: 
            message=conn.recv(2048)
            if message:
                print ("<" + addr[0] + "> " + message)
        except:
            continue

while True:
    conn, addr = server.accept()
    print("Accepted new connection!") #, conn, addr)
 
    """Maintains a list of clients for ease of broadcasting
    a message to all available people in the chatroom"""
    list_of_clients.append(conn)
    # prints the address of the user that just connected
    print (addr[0] + " connected")
 
    # creates and individual thread for every user
    # that connects
    print("starting new thread")
    start_new_thread(clientthread,(conn,addr))    
 