import socket
import threading
import logging
logging.basicConfig(
    filename="logs/server.log",
    level=logging.INFO,
    format="%(asctime)s %(message)s"
)

from auth import verify
from db import (
    save_message,
    log_activity
)

HOST = "127.0.0.1"
PORT = 6000

clients = {}

# ---------------- BROADCAST ----------------
def broadcast(sender, message):

    for user, conn in clients.items():

        if user != sender:

            try:
                conn.send(
                    f"[PUBLIC] {sender}: {message}".encode()
                )

            except:
                pass

# ---------------- PRIVATE MESSAGE ----------------
def private_message(sender, target, message):

    if target in clients:

        try:
            clients[target].send(
                f"[PRIVATE] {sender}: {message}".encode()
            )

        except:
            pass

# ---------------- HANDLE CLIENT ----------------
def handle_client(conn, addr):

    try:

        conn.send("TOKEN:".encode())

        token = conn.recv(4096).decode()

        user = verify(token)

        if not user:

            conn.send("AUTH FAILED".encode())
            conn.close()
            return

        clients[user] = conn

        conn.send(
            f"Welcome {user}".encode()
        )

        # LOGIN ACTIVITY
        log_activity(user, "login")

        while True:

            msg = conn.recv(4096).decode()

            if not msg:
                break

            # PRIVATE MESSAGE
            if msg.startswith("/pm"):

                parts = msg.split(" ", 2)

                if len(parts) < 3:
                    continue

                target = parts[1]
                private_msg = parts[2]

                private_message(
                    user,
                    target,
                    private_msg
                )

                save_message(
                    user,
                    target,
                    private_msg,
                    "private"
                )

                log_activity(
                    user,
                    "private_message"
                )

            else:

                broadcast(user, msg)

                save_message(
                    user,
                    "public",
                    msg,
                    "public"
                )

                log_activity(
                    user,
                    "public_message"
                )

    except Exception as e:
        print("ERROR:", e)

    finally:

        if 'user' in locals():
            clients.pop(user, None)

        conn.close()

# ---------------- START SERVER ----------------
def start_server():

    server = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM
    )

    server.bind((HOST, PORT))

    server.listen()

    print(f"Server running on {HOST}:{PORT}")

    while True:

        conn, addr = server.accept()

        threading.Thread(
            target=handle_client,
            args=(conn, addr),
            daemon=True
        ).start()

if __name__ == "__main__":
    start_server()
