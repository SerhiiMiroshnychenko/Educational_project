import socket
import random
from threading import Thread
from datetime import datetime
from colorama import Fore, init
import sys

init()

colors = [Fore.BLUE, Fore.CYAN, Fore.GREEN, Fore.LIGHTBLACK_EX,
          Fore.LIGHTBLUE_EX, Fore.LIGHTCYAN_EX, Fore.LIGHTGREEN_EX,
          Fore.LIGHTMAGENTA_EX, Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX,
          Fore.LIGHTYELLOW_EX, Fore.MAGENTA, Fore.RED, Fore.WHITE, Fore.YELLOW
          ]

client_color = random.choice(colors)

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 65432
seperator_token = '<SEP>'

INFORMATION = """All commands list:
/list - get all exists rooms
/create - create new room with password
/change - set new name to your room
/join - enter to room
/leave - exit room
/nickname - change your name
/help - print all available commands
/exit - close program"""


def listen_message(connection):
    try:
        while True:
            if message := connection.recv(1024).decode('utf-8'):
                print(f'\n{message}')
            else:
                print('Close program')
                sys.exit()
    except ConnectionAbortedError:
        print('Close connection.')


def send_message(client, color, letter, token):
    date_now = datetime.now().strftime('%d.%m %H:%M')
    message = f"{color}[{date_now}] {client}{seperator_token}{letter}{token}{Fore.RESET}"
    s.send(message.encode('utf-8'))



with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    print(f"[*] Connecting to {SERVER_HOST}:{SERVER_PORT}...")
    s.connect((SERVER_HOST, SERVER_PORT))
    print("[+] Connected.")
    name = input('Please, enter you nickname: ')
    thread = Thread(target=listen_message, args=(s,), daemon=True)
    thread.start()
    print(INFORMATION)
    while True:
        message = input()
        match message:
            case '/nickname':
                name = input('Please, enter you nickname: ')
                print(f'Your name now is {name}')
            case '/help':
                print(INFORMATION)
            case '/create':
                room_name = input('Please, enter new room\'s name: ')
                password = input('Please, enter new room\'s password: ')
                message = f'/create|{room_name}|{password}'
                send_message(name, client_color, message, seperator_token)
            case '/change':
                room_new_name = input('Please, enter a new name for the room: ')
                message = f'/change|{room_new_name}'
                send_message(name, client_color, message, seperator_token)
            case '/join':
                room_name = input('Please, enter room\'s name: ')
                password = input('Please, enter room\'s password: ')
                message = f'/join|{room_name}|{password}'
                send_message(name, client_color, message, seperator_token)
            case '/exit':
                break
            case _:
                send_message(name, client_color, message, seperator_token)

    s.send(letter:= f"{seperator_token}{'/exit'}".encode('utf-8'))
    print('Goodbye!')
    sys.exit()
