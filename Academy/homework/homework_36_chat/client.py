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
            if msg := connection.recv(1024).decode('utf-8'):
                print(f'\n{msg}')
            else:
                print('Close program.')
                sys.exit()
    except ConnectionAbortedError:
        print('Close connection.')


def send_message(client, color, letter_, token):
    date_now = datetime.now().strftime('%d.%m %H:%M')
    msg = f"{color}[{date_now}] {client}{seperator_token}{letter_}{token}{Fore.RESET}"
    s.send(msg.encode('utf-8'))


def create_message():
    return f'/create|{input("Please, enter new name for the room: ")}|{input("Please, create password: ")}'


def change_message():
    return f'/change|{input("Please, enter a new name for the room: ")}'


def join_message():
    return f'/join|{input("Please, enter name of the room: ")}|{input("Please, create password: ")}'


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
            case '/help':
                print(INFORMATION)
            case '/exit':
                break
            case '/nickname':
                name = input('Please, enter you nickname: ')
                print(f'Your name now is {name}')
                continue
            case '/create':
                message =  create_message()
            case '/change':
                message = change_message()
            case '/join':
                message = join_message()
        send_message(name, client_color, message, seperator_token)

    s.send(letter:= f"{seperator_token}{'/exit'}".encode('utf-8'))
    print('Goodbye!')
    sys.exit()
