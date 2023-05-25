import select
import socket


def main() -> None:
    host = socket.gethostname()
    port = 12345

    # create a TCP/IP socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.setblocking(0)
        # bind the socket to the port
        sock.bind((host, port))
        # listen for incoming connections
        sock.listen(5)
        print("Server started...")

        # sockets from which we expect to read
        inputs = [sock]
        outputs = []

        while inputs:
            # wait for at least one of the sockets to be ready for processing
            readable, writable, exceptional = select.select(inputs, outputs, inputs)

            for s in readable:
                if s is sock:
                    conn, addr = s.accept()
                    inputs.append(conn)
                elif data := s.recv(1024):
                    print(data)
                else:
                    inputs.remove(s)
                    s.close()

if __name__ == "__main__":
    main()
