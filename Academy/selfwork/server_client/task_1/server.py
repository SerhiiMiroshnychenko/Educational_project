import socket

# localhost 0.0.0.0, 127.0.0.1
HOST = '127.0.0.1'
PORT = 65432

with socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM) as s:
    s.bind((HOST, PORT))
    print("UDP server up and listening!")
    s.listen()
    connection, address = s.accept()
    while connection:
        print(f'Connected with {address}')
        while True:
            if data := connection.recv(1024):
                connection.sendall(data.upper())
            else:
                break
