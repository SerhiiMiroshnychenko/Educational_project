import socket

HOST     = "127.0.0.1"
PORT   = 20001
buffer_size  = 1024

# Create a datagram socket
udp_server_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Bind to address and ip
udp_server_socket.bind((HOST, PORT))

print(f'UDP server with HOST: {HOST} and PORT: {PORT} up and listening!')
counter = 0

# Listen for incoming datagrams
while True:
    if counter == 0:
        msg_from_server = f'Hello UDP Client! Connection with You for the {counter+1}st time!'
    else:
        msg_from_server = f'Connection with the UDP Client for the {counter+1}st time!'

    bytes_to_send = str.encode(msg_from_server)
    bytes_address_pair = udp_server_socket.recvfrom(buffer_size)
    message = bytes_address_pair[0]
    address = bytes_address_pair[1]
    if counter == 0:
        client_ip  = "Client IP Address:{!r}".format(address)
        print(client_ip)
        client_msg = f'Greeting from Client: "{message.decode()}".'

    else:
        client_msg = f'Message № {counter} from Client: "{message.decode()}".'
    print(client_msg)

    # Sending a reply to client
    udp_server_socket.sendto(bytes_to_send, address)

    counter += 1
