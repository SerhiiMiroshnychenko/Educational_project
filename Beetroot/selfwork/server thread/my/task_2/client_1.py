import socket


def main():
    server_address_port = ("127.0.0.1", 20001)
    buffer_size = 1024

    # Create a UDP socket at client side
    udp_client_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    udp_client_socket.connect(server_address_port)

    while True:

        msg_from_client = input('Please enter your message: ')
        if msg_from_client == 'exit':
            break

        udp_client_socket.send(msg_from_client.encode('ascii'))
        data = udp_client_socket.recv(buffer_size)
        print('Received from the server :', data.decode('ascii'))

    udp_client_socket.close()

if __name__ == "__main__":
        main()

