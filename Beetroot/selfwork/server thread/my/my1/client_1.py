import socket


def main():

    host     = "127.0.0.1"
    port   = 20001

    client_one = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # connect to server on local computer
    client_one.connect((host, port))


    while True:
        message = input('Please enter your message: ')
        if message == 'exit':
            break

        # message sent to server
        client_one.send(message.encode('ascii'))

        # message received from server
        data = client_one.recv(1024)

        # print the received message
        # here it would be a reverse of sent message
        print('Received from the server :', data.decode('ascii'))


    # close the connection
    client_one.close()


if __name__ == '__main__':
    main()