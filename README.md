# Memcached Lite from scratch

Memcached is a distributed memory system that reduces the load on the database and increases the rate with the web applications can fetch and store data. In this assignment, a lite version of memcached server has been implemented. In this version of the server stores and retrieves a pair of key-value from multiple clients concurrently. Contrasting to the traditional memcache, in this version, this key-value pair is stored on a file system, which makes it easier for the clients to store the data even after the server process dies.

### Design Details
This memcached-lite storage system has two attributes, one, server and second, client(s). The server is the central processing unit of the entire system. All the communication between clients, take place via server. The server and clients are implemented using socket, which acts as an endpoint in a two-way communication system. A socket is the link between two programs running on a network, by binding itself to a port number so that the TCP layer can identify it. The server process starts by setting up a socket, by choosing one of the address families

##### server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

Then the server is bound to an IP Address and a HOST, and eventually start listening on this IP and HOST,
##### server_socket.bind((IP, PORT))
##### server_socket.listen()

Now, the server is ready to receive connection and clients can connect to it by binding itself to the corresponding IP and PORT. The server will keep listening and as soon as the client connects to the server, and it will continue to receive the messages until the connection is broken by either the client or the server.
The python standard library provides threading which is the main building block for concurrently running processes, using thread the server is able to monitor multiple clients simultaneously. To start a separate thread, Thread instance is created and then is initialized by .start().
On the client side, the socket is connected to the server IP and PORT using the function client_socket.connect. After the connection is established, the server and client are able to exchange key value pairs. To exit the client, exit function has been defined.

The commands implemented are as follows,
1. Set
For this command server accepts input from the client in the following format:

set <key> <value-size-bytes> \r\n
<value> \r\n

As soon as the SET command is encountered by the server, it checks the length of the input, if the length of the input is < 4, it throws an error, as INVALID COMMAND. Server also checks type of value-size-bytes , if it is of type int, it will then check if the length of the value is smaller than or equal to it, it will respond with NOT STORED. The server responds with STORED if the key-value pair has been stored in a local dictionary and CSV file.

2. Get
For this command server accepts input from the client as GET <key> and in response, the server responds with if the value is available in the file storage system. 
  
VALUE <key> <value>\r\n
END\n

If the value is not found on the file system, the server responds with, NOT FOUND. To run the server and client, there are two .py files in the folder, server.py and client.py. These files can be run on a terminal by using the following commands:

Terminal 1: python3 server.py Terminal 2: python3 client.py

As soon as the server and the process starts, the serversocket sends a message to the client socket as “Client Socket”. From here on, users can start using client this as mimic of a memcached client. This memcached client key-value store is implemented using SET and GET commands in the following format:

SET <KEY> <SIZE> \n
<VALUE>

Where KEY and VALUE can be string/integers and SIZE is in integer. On hitting the Enter key, the client will be notified with the status of STORED/NOT STORED. For successfully storing the key-value, make sure the len(value)<=size.

The GET command on this memcached client returns the latest VALUE of the KEY. Its syntax
is,

GET <KEY>\n

Output for the GET command will be:
VALUE <KEY> <VALUE>\n
END
