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
    while True:
        if message := connection.recv(1024).decode('utf-8'):
            print(f'\n{message}')
        else:
            print('Close program')
            sys.exit()


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
        if message == '/nickname':
            name = input('Please, enter you nickname: ')
            print(f'Your name now is {name}')
        elif message == '/help':
            print(INFORMATION)
        elif message == '/exit':
            date_now = datetime.now().strftime('%d.%m %H:%M')
            message = f"{client_color}[{date_now}] {name}{seperator_token}{message}{seperator_token}{Fore.RESET}"
            s.send(message.encode('utf-8'))
            print('Close program')
            sys.exit()
        else:
            date_now = datetime.now().strftime('%d.%m %H:%M')
            message = f"{client_color}[{date_now}] {name}{seperator_token}{message}{seperator_token}{Fore.RESET}"
            s.send(message.encode('utf-8'))

