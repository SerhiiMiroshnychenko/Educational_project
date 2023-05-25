"""
PIPE
"""


import multiprocessing
import os


def sender(conn, msgs):
    for msg in msgs:
        conn.send(msg)
        print(f"Sent the message: {msg} from process {os.getpid()}")
    conn.close()


def receiver(conn):
    while True:
        msg = conn.recv()
        if msg == "END":
            break
        print(f"Received the message: {msg} in process {os.getpid()}")


msgs = ["hello", "hey", "hru?", "END"]

# creating a pipe
parent_conn, child_conn = multiprocessing.Pipe()

def main():
    # creating new processes
    p1 = multiprocessing.Process(target=sender, args=(parent_conn, msgs))
    p2 = multiprocessing.Process(target=receiver, args=(child_conn,))

    p1.start()
    p2.start()
    p1.join()
    p2.join()


if __name__ == "__main__":
    main()
