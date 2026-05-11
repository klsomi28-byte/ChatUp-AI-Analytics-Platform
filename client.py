import socket
import threading

HOST = "127.0.0.1"
PORT = 6000

# ---------------- LISTENER ----------------
def receive(sock):

    while True:

        try:

            msg = sock.recv(4096).decode()

            print("\n" + msg)

        except:
            break

# ---------------- START CLIENT ----------------
def start():

    sock = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM
    )

    sock.connect((HOST, PORT))

    print(sock.recv(1024).decode())

    token = input("Enter JWT Token: ")

    sock.send(token.encode())

    threading.Thread(
        target=receive,
        args=(sock,),
        daemon=True
    ).start()

    while True:

        msg = input()

        sock.send(msg.encode())

if __name__ == "__main__":
    start()
