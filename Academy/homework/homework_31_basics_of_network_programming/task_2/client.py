import socket


HOST = '127.0.0.1'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        text = input('Enter your text: ')
        if text == 'exit':
            break
        bias = input('Enter bias: ')
        message = f'{text}#{bias}'
        s.sendall(message.encode('utf8'))
        data = s.recv(1024)
        print(f"Server's echo: <{data.decode('utf8')}>.")
