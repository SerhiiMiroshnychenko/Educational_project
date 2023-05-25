"""
Task 3

Echo server with multiprocessing
Create a socket echo server that handles each
connection using the multiprocessing library.
"""

import socket
import multiprocessing


print_lock = multiprocessing.RLock()

def processed(letter, client_id):
    while True:
        data = letter.recv(1024)
        if not data:
            print(f'Goodbye Client {client_id}!')
            break

        print(f'Message from Client {client_id}: {data.decode("ascii").upper()}')
        data = b'FROM ME TO YOU "' + data.upper() + b'" TOO'

        letter.send(data)

    letter.close()


def main():

    host     = "127.0.0.1"
    port   = 20001

    main_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    main_server.bind((host, port))
    print("Socket bound to port:", port)

    main_server.listen(5)
    print("Socket is listening:")

    while True:
        message, address = main_server.accept()

        print_lock.acquire()
        print('Connected to :', address[1])

        multiprocessing.Process(target=processed, args=(message, address[1])).start()


if __name__ == '__main__':
    main()
