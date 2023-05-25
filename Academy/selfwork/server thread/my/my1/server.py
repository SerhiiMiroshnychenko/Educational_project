# import socket programming library
import socket

# import thread module
from _thread import start_new_thread
import threading

print_lock = threading.RLock()


# thread function
def threaded(letter, client_id):
    while True:

        # data received from client
        data = letter.recv(1024)
        if not data:
            print(f'Goodbye Client {client_id}!')

            # lock released on exit
            # print_lock.release()
            break

        # reverse the given string from client
        print(f'Message from Client {client_id}: {data.decode("ascii").upper()}')
        data = b'FROM ME TO YOU "' + data.upper() + b'" TOO'

        # send back reversed string to client
        letter.send(data)

    # connection closed
    letter.close()


def main():

    host     = "127.0.0.1"
    port   = 20001

    main_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    main_server.bind((host, port))
    print("Socket bound to port:", port)

    # put the socket into listening mode
    main_server.listen(5)
    print("Socket is listening:")

    # a forever loop until client wants to exit
    while True:
        # establish connection with client
        message, address = main_server.accept()

        # lock acquired by client
        print_lock.acquire()
        print('Connected to :', address[1])

        # Start a new thread and return its identifier
        start_new_thread(threaded, (message, address[1]))
    main_server.close()


if __name__ == '__main__':
    main()