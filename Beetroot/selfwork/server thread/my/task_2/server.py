# Task 2

# Echo server with threading

# Create a socket echo server which handles each connection in a separate Thread

import socket
import threading
from _thread import start_new_thread

print_lock = threading.RLock()

def threaded(letter):
    while True:

        # data received from client
        data = letter.recv(1024)
        if not data:
            print('Bye')

            # lock released on exit
            print_lock.release()
            break

        # reverse the given string from client
        data = data.upper()

        # send back reversed string to client
        letter.send(data)

    # connection closed
    letter.close()


def main():
    host = "127.0.0.1"
    port = 20001
    buffer_size = 1024

    # Create a datagram socket
    udp_server_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

    # Bind to address and ip
    udp_server_socket.bind((host, port))

    print(f'UDP server with HOST: {host} and PORT: {port} up and listening!')

    msg_from_server = 'OK UDP Client!'

    udp_server_socket.listen(5)
    print("Socket is listening")
    # Listen for incoming datagrams
    while True:


        bytes_to_send = str.encode(msg_from_server)
        bytes_address_pair = udp_server_socket.accept()
        message, address = bytes_address_pair

        print_lock.acquire()

        client_ip = "ip<{!r}>".format(address[1])
        client_msg = f'Message from Client {client_ip}: "{message}".'
        print(client_msg)

        # Sending a reply to client
        udp_server_socket.sendto(bytes_to_send, address)

        start_new_thread(threaded, (message,))
    udp_server_socket.close()


if __name__ == "__main__":
    main()