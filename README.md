# p2p-chat

## How it works:

This is a p2p chat application using python sockets. One of the scripts creates a rendezvous server that listens on all ports for a client to connect to the server. Once a client connects it adds them to a list and waits for a second connection. Once another client connects it pairs the two clients. Then the clients are able to communicate with each other. After the client sends or receives a message it is also logged into a local SQL database that is stored in the directory where the scripts are located.

## Requirements:
-SQLite3

## How to use:

1. Each client should run "create_db.py" to create a local SQL database.
2. The rendevous server must be started with "youtube-server.py" and you will need to choose a port and indicate it as an argument when you run the file.
3. Each client will need to get the the IP address of the rendevous server and the port then pass those as arguments to the "youtube-client.py" script. i.e. python3 youtube-client.py 192.41.123.1 55555
4. Then each client can communicate with the other via the terminal!
5. The values of the messages will be automatically stored in the 
