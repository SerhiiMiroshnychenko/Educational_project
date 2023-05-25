import socket


def main():

    host     = "127.0.0.1"
    port   = 20001

    client_one = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_one.connect((host, port))

    while True:
        message = input('Please enter your message: ')
        if message == 'exit':
            break

        client_one.send(message.encode('ascii'))
        data = client_one.recv(1024)

        print('Received from the server :', data.decode('ascii'))

    client_one.close()


if __name__ == '__main__':
    main()
