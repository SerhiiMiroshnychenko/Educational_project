import socket
from threading import Thread
import time

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 65432
seperator_token = '<SEP>'

client_sockets = {}  # {connection: {role: 'admin/base', room: room_name}}
rooms = {'default': ''}  # room_name: password

def manage_commands(command, client):
    if command == '/list':
            return 'All available rooms:'+'\n'.join(rooms.keys())
    elif command.startswith('/create'):
        command, name, password = tuple(command.split('|'))
        rooms[name] = password
        client_sockets[client] = {'role': 'admin', 'room': name}
        return ''
    elif command.startswith('/change'):
        command, new_name = tuple(command.split('|'))
        if client_sockets[client]['role'] == 'admin':
            old_name = client_sockets[client]['room']
            client_sockets[client]['room'] = new_name
            rooms[new_name] = rooms[old_name]
            del rooms[old_name]
        return ''
    elif command.startswith('/join'):
        command, name, password = tuple(command.split('|'))
        if rooms[name] == password:
            client_sockets[client]['room'] = name
        return ''
    elif command == '/leave':
        client_sockets[client]['room'] = 'default'

def listen_message(client):
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            clear_massage = message.split(seperator_token)[1]
            if not clear_massage.startswith('/exit'):
                manage_commands(clear_massage, client)
            else:
                del client_sockets[client]
                client.close()
                time.sleep(1)
                break

        except Exception as error:
            print(f'[!] Error: {error}')
            del client_sockets[client]
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
        client_sockets.setdefault(client_socket, {'role': 'base', 'room': 'default'})
        thread = Thread(target=listen_message, args=(client_socket,), daemon=True)
        thread.start()
