# Task 2

# Extend the echo server, which returns to client the data,
# encrypted using the Caesar cipher algorithm by a specific
# key obtained from the client.


import socket
from ceasar import caesar  # type: ignore

HOST = '127.0.0.1'
PORT = 65432

print(f'UDP server with HOST: {HOST} and PORT: {PORT} up and listening!')

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    connection, address = s.accept()
    while connection:
        print(f'Connected with {address}')
        while data := connection.recv(1024):
            text, bias = data.decode('utf8').split('#')
            result = caesar(text, int(bias)).encode('utf8')
            connection.sendall(result)
