import sqlite3
from sqlite3 import Error
from datetime import datetime

connection_obj = sqlite3.connect('p2pchat.db')
cur = connection_obj.cursor()


my_ip = '1.0.0.0'
peer_ip = '1.0.1.1'
data = 'Hello!'
now = datetime.now()
cur_time  = now.strftime("%m/%d/%Y, %H:%M:%S")


cur.execute(f"INSERT INTO CHAT(SOURCE, DEST, MESSAGE, TIME) VALUES ('{peer_ip}', '{my_ip}', '{data}', '{cur_time}')")

print("Inserted message into database")
# Fetch data to test if it was inserted 
rows = cur.execute("SELECT * FROM CHAT").fetchall()

print(len(rows))
print("DATABASE CONTENTS:")
for row in rows:
    print(row)

connection_obj.commit()

connection_obj.close()