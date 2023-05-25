import socket
import threading
from threading import Thread

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 65432
seperator_token = '<SEP>'

rooms = {'default': ''}  # room_name: password
client_sockets = {}  # {connection: {role: 'admin'/'base', room: room_name}

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

def server_log(letter, seperator):
    cl_message = ''
    try:
        cl_message = letter.split(seperator)[1]
        client_ = (letter.split(seperator)[0]).split(' ')[2]
        tread_ = threading.current_thread().name.split(' ')[0]
        print(f'{tread_}({client_}): "{cl_message}"')
    except IndexError:
        print('The client has logged out.')
    return cl_message


def prepare_message(letter, token):
    message = letter.replace(token, ': ')
    second_token = message.rfind(':')
    return message[:second_token] + message[second_token + 2:]


def listen_message(client):
    while True:
        message = ''
        try:
            message = client.recv(1024).decode('utf-8')
            clear_message = server_log(message, seperator_token)
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
            message = prepare_message(message, seperator_token)
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
