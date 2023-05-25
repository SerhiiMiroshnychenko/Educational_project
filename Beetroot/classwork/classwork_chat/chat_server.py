import socket
from threading import Thread

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 65432
seperator_token = '<SEP>'

client_sockets = set()


def listen_message(client):
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
        except Exception as error:
            print(f'[!] Error: {error}')
            client_sockets.remove(client)
            message = ''
        else:
            message = message.replace(seperator_token, ': ')
        for value in client_sockets:
            value.send(message.encode('utf-8'))


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((SERVER_HOST, SERVER_PORT))
    s.listen(5)
    print(f"[*] Listening as {SERVER_HOST}:{SERVER_PORT}")
    while True:
        client_socket, client_address = s.accept()
        print(f"[+] {client_address} connected.")
        client_sockets.add(client_socket)
        thread = Thread(target=listen_message, args=(client_socket,), daemon=True)
        thread.start()
