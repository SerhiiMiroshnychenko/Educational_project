import socket


def main():

    host     = "127.0.0.1"
    port   = 20001

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # connect to server on local computer
    s.connect((host, port))

    # message you send to server
    message = "Here is Client Two!"
    while True:

        # message sent to server
        s.send(message.encode('ascii'))

        # message received from server
        data = s.recv(1024)

        # print the received message
        # here it would be a reverse of sent message
        print('Received from the server :', data.decode('ascii'))

        # ask the client whether he wants to continue
        ans = input('\nDo you want to continue(y/n) :')
        if ans == 'y':
            continue
        else:
            break
    # close the connection
    s.close()


if __name__ == '__main__':
    main()