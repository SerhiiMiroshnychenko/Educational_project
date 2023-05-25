import socket

HOST = '127.0.0.1'  # Standard loop-back interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

sock = socket.socket()
sock.bind((HOST, PORT))
sock.listen(1)
conn, addr = sock.accept()

print('Connected by', addr)

while True:
    data = conn.recv(1024)
    if not data:
        break
    conn.send(data.upper())

conn.close()
