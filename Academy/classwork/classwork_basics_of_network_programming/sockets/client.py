import socket


HOST = '127.0.0.1'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        message = input('Enter your text: ')
        if message == 'exit':
            break
        s.sendall(message.encode('utf8'))
        data = s.recv(1024)
        print(f"Server's echo {data.decode('utf8')}")



