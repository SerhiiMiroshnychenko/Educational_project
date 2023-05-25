import socket
import threading
import time
from threading import Thread

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 65432
seperator_token = '<SEP>'

rooms = {'default': ''}  # room_name: password
client_sockets = {}  # {connection: {role: 'admin'/'base', room: room_name}


# /list - get all exists rooms
# /create - create new room with password
# /change - set new name to your room
# /join - enter to room
# /leave - exit room
# /exit - close program

def manage_commands(command, client):
    if command.startswith('/list'):
        return 'All available rooms: \n' + '\n'.join(rooms.keys())
    elif command.startswith('/create'):
        command, name, password = tuple(command.split('|'))
        rooms[name] = password
        client_sockets[client] = {'role': 'admin', 'room': name}
        return f'Crated new room with name {name}'
    elif command.startswith('/change'):
        return rename_room(command, client)
    elif command.startswith('/join'):
        command, name, password = tuple(command.split('|'))
        if rooms[name] != password:
            return 'Wrong password'
        client_sockets[client]['room'] = name
        return f'Joined to {name} room'
    elif command.startswith('/leave'):
        client_sockets[client]['room'] = 'default'
        return 'Exit room'
    else:
        return ''


def rename_room(command, client):
    command, new_name = tuple(command.split('|'))
    if client_sockets[client]['role'] != 'admin':
        return 'You are not admin'
    old_name = client_sockets[client]['room']
    client_sockets[client]['room'] = new_name
    rooms[new_name] = rooms[old_name]
    del rooms[old_name]
    return f'Changed room\'s name from {old_name} to {new_name}'


def listen_message(client):
    while True:
        message = ''
        try:
            message = client.recv(1024).decode('utf-8')
            clear_message = ''
            try:
                clear_message = message.split(seperator_token)[1]
                client_ = (message.split(seperator_token)[0]).split(' ')[2]
                print(f'{threading.current_thread().name}: {client_}: "{clear_message}"')
            except IndexError:
                print('The client has logged out.')
            if clear_message and clear_message.startswith('/'):
                if clear_message.startswith('/exit'):
                    break
                result = manage_commands(clear_message, client)
                client.send(result.encode('utf-8'))
                continue
        except Exception as error:
            print(f'[!] Error: {error}')
            try:
                del client_sockets[client]
                message = ''
            except KeyError:
                print('The client has logged out.')
        else:
            message = message.replace(seperator_token, ': ')
            second_token = message.rfind(':')
            message = message[:second_token]+message[second_token+2:]
        try:
            client_room = client_sockets[client]['room']
        except KeyError as error:
            print(error.__class__, error)
        try:
            for connection in filter(lambda x: client_sockets[x]['room'] == client_room, client_sockets):
                connection.send(message.encode('utf-8'))
        except NameError as error:
            print(error.__class__, error)
    try:
        del client_sockets[client]
        client.close()
    except KeyError as error:
            print(error.__class__, error)


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
