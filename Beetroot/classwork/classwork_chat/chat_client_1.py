import socket
import random
from threading import Thread
from datetime import datetime
from colorama import Fore, init

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


def listen_message(connection):
    while True:
        message = connection.recv(1024).decode('utf-8')
        print(f'\n{message}')


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    print(f"[*] Connecting to {SERVER_HOST}:{SERVER_PORT}...")
    s.connect((SERVER_HOST, SERVER_PORT))
    print("[+] Connected.")
    name = input('Please, enter you nickname: ')
    thread = Thread(target=listen_message, args=(s,))
    thread.start()
    while True:
        message = input()
        date_now = datetime.now().strftime('%d.%m %H:%M')
        message = f"{client_color}[{date_now}] {name}{seperator_token}{message}{Fore.RESET}"
        s.send(message.encode('utf-8'))
