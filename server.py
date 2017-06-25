import socket

# decalring th HOST and PORT value
HOST, PORT = 'localhost', 8888

# establishing the maxium size of data to pass through
max_size = 1024

# setting up the socket fo the server; binding the host address and port
_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
_socket.bind((HOST, PORT))

# setting how many connections to take
_socket.listen(5)

print("Listening on port %s" % ( PORT ))


client_connection, client_address = _socket.accept()

# displaying the client/s address
print('[ Client Address: <%s:%d> ]' % ( client_address[0], client_address[1] ))

# holginthe server response to send to the client/s
server_response = ''
while server_response != 'kill' or server_response != 'q':

    # Getting the request data from client/s
    client_request = client_connection.recv( max_size ).decode('utf-8')
    print('\n> %s' % ( client_request ) )

    # sending back response to client/s
    server_response = input('server:%s:%d$ ' % ( HOST, PORT ))
    client_connection.send(bytes(server_response.encode('utf-8')))

# closing client/s conection
client_connection.close()
