import socket


def main():

    host     = "127.0.0.1"
    port   = 20001

    client_one = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_one.connect((host, port))
    counter = 1

    while True:

        message = f"Have a good day in {counter} time!"

        client_one.send(message.encode('ascii'))
        data = client_one.recv(1024)

        print('Received from the server :', data.decode('ascii'))

        answer = input('\nDo you want to continue (y/n): ')
        if answer == 'y':
            counter += 1
        else:
            break

    client_one.close()


if __name__ == '__main__':
    main()
