import socket
import sys
import threading
import sqlite3
from sqlite3 import Error
from datetime import datetime
import sys

rendezvous = ('10.192.49.109', 55555)
# connect to your database
connection_obj = sqlite3.connect('p2pchat.db')
cur = connection_obj.cursor()

# connect to rendezvous
print('connecting to rendezvous server')

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('0.0.0.0', 50001))
sock.sendto(b'0', rendezvous)

while True:
    data = sock.recv(1024).decode()

    if data.strip() == 'ready':
        print('checked in with server, waiting')
        break

data = sock.recv(1024).decode()
ip, sport, dport = data.split(' ')
sport = int(sport)
dport = int(dport)

print('\ngot peer')
print('  ip:          {}'.format(ip))
print('  source port: {}'.format(sport))
print('  dest port:   {}\n'.format(dport))

my_ip = str(socket.gethostbyname(socket.gethostname()))
peer_ip = str(ip) # this will be used in DB writes

# punch hole
# equiv: echo 'punch hole' | nc -u -p 50001 x.x.x.x 50002
print('punching hole')

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('0.0.0.0', sport))
sock.sendto(b'0', (ip, dport))
sock.close()

print('ready to exchange messages\n')

# listen for
# equiv: nc -u -l 50001
def listen():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print("PORT:", sport)
    sock.bind(('0.0.0.0', sport))

    while True:
        data = sock.recv(1024)
        data = data.decode()
        # ADD MESSAGE TO DB
        now = datetime.now()
        cur_time  = now.strftime("%m/%d/%Y, %H:%M:%S")
        cur.execute(f"INSERT INTO CHAT(SOURCE, DEST, MESSAGE, TIME) VALUES ('{peer_ip}', '{my_ip}', '{data}', '{cur_time}')")
        print('\rpeer: {}\n> '.format(data.decode()), end='')

listener = threading.Thread(target=listen, daemon=True);
listener.start()

# send messages
# equiv: echo 'xxx' | nc -u -p 50002 x.x.x.x 50001
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('0.0.0.0', dport))

while True:
    msg = input('> ')
    # ADD MESSAGE TO DB
    now = datetime.now()
    cur_time  = now.strftime("%m/%d/%Y, %H:%M:%S")
    cur.execute(f"INSERT INTO CHAT(SOURCE, DEST, MESSAGE, TIME) VALUES ('{my_ip}', '{peer_ip}', '{msg}', '{cur_time}')")
    sock.sendto(msg.encode(), (ip, sport))
    if msg == 'exit':
        connection_obj.commit()
        sys.exit()
