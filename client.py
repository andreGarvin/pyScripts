import socket

# decalring HOST and PORT values; Establishing the maxium size of data to pas throgh
HOST, PORT = 'localhost', 8888
max_size = 1024

# setting up the socket for the client to communicateto the server
_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# recving conection from server
_socket.connect((HOST, PORT))

# continously getting and sendig responses
while True:

    # holding the clinent/s response to send to the server
    try:
        client_response = raw_input('client:(%s:%s)$ ' % ( HOST, PORT ))
    except:
        client_response = input('client:(%s:%s)$ ' % ( HOST, PORT ))
    _socket.send(bytes(client_response.encode('utf-8')))

    server_response = _socket.recv(max_size).decode('utf-8')
    print('\n> %s' % ( server_response ) )

_socket.close()
